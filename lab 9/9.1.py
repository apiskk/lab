from PIL import Image

img=Image.open('ориг.jpg')
img.show()

print(f"Размер: {img.size[0]}x{img.size[1]}")
print(f"Формат: {img.format}")
print(f"Цветовая модель: {img.mode}")