
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont

def generate_image():
    target_date = datetime.now() + timedelta(days=45)
    now = datetime.now()
    time_remaining = target_date - now

    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    width, height = 400, 100
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    countdown_text = f"{days}d {hours}h {minutes}m {seconds}s remaining"
    bbox = draw.textbbox((0, 0), countdown_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    draw.text((text_x, text_y), countdown_text, fill=(0, 0, 0), font=font)
    image.save("countdown.png")
