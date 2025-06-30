from PIL import Image, ImageFilter
import os

if not os.path.exists('papka2.0'):
    os.mkdir('papka2.0')

for file in os.listdir():
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            img = Image.open(file)
            img2 = img.convert('L')
            new_file = os.path.join('papka2.0', f"bw_{file}")
            img2.save(new_file)
            print(f"готово:{file}")
        except Exception as e:
            print("oшибка")