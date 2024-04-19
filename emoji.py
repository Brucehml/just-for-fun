from PIL import Image, ImageDraw, ImageFont
import random

#2024.4.10
#2024.4.19
emojis = ["❤️", "?", "?", "?", "?", "?", "?"]
font = ImageFont.truetype("arial.ttf", 64)
input_text = "I love Python!"

def get_emoji(text):
    return random.choice([e for e in emojis if text.lower().count(e.lower())]>0])

def get_image(emoji, text):
    img = Image.new("RGB", (700, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((50, 100), text, font=font, fill=(0, 0, 0))
    emoji_image = Image.open(f"emoji_images/{emoji}.png")
    emoji_image = emoji_image.resize((100, 100))
    img.paste(emoji_image, (600, 50))
    img.show()


emoji = get_emoji(input_text)
get_image(emoji, input_text)
