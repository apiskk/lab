from PIL import Image

prazdnik = {
    "праздников котиков": "открытка.jpg",
    "нг": "открытка2.0.jpg",
    "др": "открытка3.0.jpg"
}

i = input("К какому празднику открытка? (др/нг/праздников котиков): ").lower()

if i in prazdnik:
    try:
        img = Image.open(prazdnik[i])
        img.show()
        print("готово")
    except:
        print("нет открытки")
else:
    print("нет такого праздника")