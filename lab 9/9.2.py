from PIL import Image
img=Image.open('ориг.jpg')

#уменьшение
minimg=img.resize((img.width // 3, img.height // 3))
minimg.save("mini.jpg")

#зеркало
goriz = img.transpose(Image.FLIP_LEFT_RIGHT)
vertik = img.transpose(Image.FLIP_TOP_BOTTOM)
goriz.save("зеркало_горизонтальное.jpg")
vertik.save("зеркало_вертикальное.jpg")