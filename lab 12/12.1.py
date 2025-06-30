import json

with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for product in data['products']:
    print("Название:", product['name'])
    print("Цена:", product['price'])
    print("Вес:", product['weight'])
    if product['available'] == True:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()