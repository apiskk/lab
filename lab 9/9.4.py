from PIL import Image, ImageDraw, ImageFont
import os

def add_water(img_path, out_path, text):
    img = Image.open(img_path)
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()

    w, h = img_copy.size
    x = w // 2
    y = h // 2

    color = (255, 255, 255, 50)
    draw.text((x, y), text, font=font, fill=color, anchor="mm")

    img_copy.save(out_path)

if __name__ == "__main__":
    in_img = "ориг.jpg"
    out_img = "с маркой.jpg"
    mark = "ироппгр"

    add_water(in_img, out_img, mark)
    print(f"готово {out_img}")