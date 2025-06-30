capital = {
    'Россия': 'Москва',
    'США': 'Вашингтон',
    'Япония': 'Токио',
    'Франция': 'Париж',
    'Италия': 'Рим',
    'Германия': 'Берлин',
}
#a
print ('Список стран и их столиц:')
for name in capital:
    print(f'{name}-{capital[name]}')

#b
name=input('Введи название страны:')
if name in capital:
    print(f'Столица {name}: {capital[name]}')
else:
    print('ошибка')
#c
print ('Сортированный список:')
for name in sorted(capital):
    print(f'{name}: {capital[name]}')