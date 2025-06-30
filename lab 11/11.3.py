import csv
spisok = [
    ["Продукт", "Количество", "Цена"],
    ["Молоко", 1, 808],
    ["Сыр", 1, 500],
    ["Хлеб", 2, 0]
]

with open('products.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(spisok)

total = 0
print("Нужно купить:")

with open('products.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)

    for product, kolvo, price in reader:
        total += int(kolvo) * int(price)
        print(f"{product} - {kolvo} шт. за {price} руб.")

print(f"Итоговая сумма: {total} руб.")