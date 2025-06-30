from PIL import Image
import os

img = Image.open('открытка.jpg')
w,h = img.size

#универсально по центру
left = w // 4
top = h // 4
right = 3 * w// 4
bottom = 3 * h // 4

img2 = img.crop((left, top, right, bottom))
img2.save('открытка2.jpg')

print('готово')