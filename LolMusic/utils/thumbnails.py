import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch 
from config import YOUTUBE_IMG_URL

# Function for resizing images smoothly
def resize_image(image, width, height):
    return image.resize((width, height), Image.LANCZOS)

# Main Function for Thumbnail Generation
async def get_thumb(videoid):
    cache_path = f"cache/{videoid}.png"
    temp_path = f"cache/thumb{videoid}.png"
    
    # Agar pehle se bani hui hai toh wahi return karega
    if os.path.isfile(cache_path):
        return cache_path

    if not os.path.exists("cache"):
        os.makedirs("cache")

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        # Fetch Video Details
        results = VideosSearch(url, limit=1)
        res_data = await results.next()
        
        if not res_data["result"]:
            return YOUTUBE_IMG_URL

        result = res_data["result"][0]
        title = re.sub(r"\W+", " ", result.get("title", "Unsupported Title")).title()
        duration = result.get("duration", "Unknown")
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        views = result.get("viewCount", {}).get("short", "Unknown Views")

        # Download YouTube Thumbnail
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(temp_path, mode="wb") as f:
                        await f.write(await resp.read())

        # Image Processing Starts
        youtube = Image.open(temp_path).convert("RGBA")
        
        # --- LIGHT BLUE THEME COLORS ---
        GLOW_COLOR = "#00BFFF"   # Deep Sky Blue (Neon effect)
        BORDER_COLOR = "#ADD8E6" # Light Blue (Border line)
        # -------------------------------

        # 1. Background (Blurred & Darkened)
        bg = resize_image(youtube, 1280, 720)
        bg = bg.filter(ImageFilter.GaussianBlur(25))
        bg = ImageEnhance.Brightness(bg).enhance(0.4)

        # 2. Main Thumbnail (Rounded Corners)
        thumb_width, thumb_height = 840, 460
        main_thumb = resize_image(youtube, thumb_width, thumb_height)
        
        mask = Image.new("L", (thumb_width, thumb_height), 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.rounded_rectangle([(0, 0), (thumb_width, thumb_height)], radius=30, fill=255)
        main_thumb.putalpha(mask)

        center_x, center_y = 640, 320
        thumb_x = center_x - (thumb_width // 2)
        thumb_y = center_y - (thumb_height // 2)

        # 3. Light Blue Glow Effect
        glow_layer = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        draw_glow = ImageDraw.Draw(glow_layer)
        draw_glow.rounded_rectangle(
            [(thumb_x - 15, thumb_y - 15), (thumb_x + thumb_width + 15, thumb_y + thumb_height + 15)],
            radius=40, fill=GLOW_COLOR
        )
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(25))
        bg.paste(glow_layer, (0, 0), glow_layer)

        # 4. Light Blue Border
        border_layer = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        draw_border = ImageDraw.Draw(border_layer)
        draw_border.rounded_rectangle(
            [(thumb_x - 4, thumb_y - 4), (thumb_x + thumb_width + 4, thumb_y + thumb_height + 4)],
            radius=35, fill=BORDER_COLOR
        )
        bg.paste(border_layer, (0, 0), border_layer)
        bg.paste(main_thumb, (thumb_x, thumb_y), main_thumb)

        # 5. Writing Text (Title & Stats)
        draw = ImageDraw.Draw(bg)
        
        # Font paths check karein ki ye aapke bot folder me hain ya nahi
        try:
            font_title = ImageFont.truetype("assets/font.ttf", 45)
            font_details = ImageFont.truetype("assets/font2.ttf", 32)
        except:
            font_title = ImageFont.load_default()
            font_details = ImageFont.load_default()

        if len(title) > 40:
            title = title[:37] + "..."

        # Draw Title (White Color)
        draw.text((320, 580), title, fill="white", font=font_title)
        
        # Draw Stats (Light Blue Color)
        stats_text = f"Views: {views} | Duration: {duration}"
        draw.text((320, 640), stats_text, fill=BORDER_COLOR, font=font_details)

        # Cleanup & Save
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
        bg.convert("RGB").save(cache_path, "PNG")
        return cache_path

    except Exception as e:
        print(f"Error generating thumbnail: {e}")
        return YOUTUBE_IMG_URL

# For backwards compatibility if needed
async def gen_thumb(videoid):
    return await get_thumb(videoid)
