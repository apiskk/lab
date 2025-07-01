from PIL import Image, ImageFilter
import os

if not os.path.exists('lab9'):
    os.mkdir('papka2')

for i in range(1, 6):
    try:
        pic = Image.open(f'{i}.jpg')
        pic = pic.convert('L')
        pic.save(f'papka2/{i}_done.jpg')
        print(f'Файл {i}.jpg готов')
    except:
        print('ошибка')
