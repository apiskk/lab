from PIL import Image, ImageDraw, ImageFont

prazdnik = {
    "праздников котиков": "открытка.jpg",
    "нг": "открытка2.0.jpg",
    "др": "открытка3.0.jpg"
}

i = input("к какому празднику открытка? (др/нг/праздников котиков): ").lower()
name = input("введите имя: ")

if i in prazdnik:
    try:
        img = Image.open(prazdnik[i])
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 70)
        except:
            font = ImageFont.load_default()
            font.size = 70

        text = f"{name}, поздравляю!"
        x = img.width // 2
        y = img.height // 2

        draw.text((x, y), text, font=font, fill="red", anchor="mm")

        img.save(f"поздравляю_{i}.png")
        print("готово")

    except Exception as e:
        print("ошибка")
else:
    print("такого праздника нет в списке")