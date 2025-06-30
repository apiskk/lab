import json

with open('products', 'r', encoding='utf-8') as f:
    data = json.load(f)

name = input("Введите название продукта: ")
price = float(input("Введите цену: "))
weight = float(input("Введите вес: "))
available = input("Продукт в наличии? (да/нет): ")

if available == 'да':
    available = True
else:
    available = False

new_product = {
    'name': name,
    'price': price,
    'weight': weight,
    'available': available
}

data['products'].append(new_product)

#сохраняем обратно
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


print("\nВсе продукты:\n")
for product in data['products']:
    print("Название:", product['name'])
    print("Цена:", product['price'])
    print("Вес:", product['weight'])
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()