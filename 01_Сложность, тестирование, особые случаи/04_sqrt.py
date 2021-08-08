'''
Решите в целых числах уравнение:
sqrt(ax+b) = c
a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых числах нет.

Формат ввода
Вводятся три числа a, b и c по одному в строке.

Формат вывода
Программа должна вывести все решения уравнения в порядке возрастания, либо NO SOLUTION (заглавными буквами), если решений нет. 
Если решений бесконечно много, вывести MANY SOLUTIONS. 
'''
a = int(input())
b = int(input())
c = int(input())
x = 0

if c < 0:
    print('NO SOLUTION')
else:
    if a==0:
        if b<0:
            print('NO SOLUTION')
        elif b == c**2:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        x = (c**2-b)/a
        if (a*x+b >= 0) and (x==int(x)):
            print(int(x))
        else:
            print('NO SOLUTION')
