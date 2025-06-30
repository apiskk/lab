sell={
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЁЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ШЭЮ',
    10: 'ФЩЪ'
}
slovo=input('Введите слово:').upper() #все заглавные
schet=0
for i in slovo:
    for ochko in sell: #ochko для пребора ключей-очков
        if i in sell[ochko]:
            schet+=ochko
print(f'слово "{slovo}" = {schet}')