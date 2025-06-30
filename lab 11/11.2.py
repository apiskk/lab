from PIL import Image
import os

filename = "ориг.jpg"

#расширение файла (в нижнем регистре)
file_png = os.path.splitext(filename)[1].lower()

if file_png in ['.jpg', '.jpeg', '.png']:
    try:
        img = Image.open(filename)
        img.show()

        print(f"Размер: {img.size[0]}x{img.size[1]}")
        print(f"Формат: {img.format}")
        print(f"Цветовая модель: {img.mode}")

    except FileNotFoundError:
        print("Ошибка: файл не найден!")
else:
    print("Ошибка: нужен файл формата .jpg, .jpeg или .png!")