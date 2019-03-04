long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
print(long_phrase > short_phrase)

text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
count_a = text.count('а')
count_i = text.count('и')
if count_a > count_i:
  print('Буква а встречается чаще')
else: 
    print('Буква и встречается чаще')
	
a = int(input("Введите Кбайт файла"))
b = int(1024)
c = a / b
print('Объем файла равен')
print(c)
print('Mb')

import math
a = math.radians(30)
x = math.sin(a)
print(x)

#чтобы результат был точный, нужно использовать десятичный модуль
#подробно об этом расписано по ссылке 
#https://php-academy.kiev.ua/blog/mathematical-modules-in-python-decimal-and-fractions
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))

a = 4
b = 5
a,b = b,a
print(a)
print(b)

num="10011"   
print(int(num, 2))


	