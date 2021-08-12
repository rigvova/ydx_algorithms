'''
Даны числа a, b, c, d, e, f. Решите систему линейных уравнений:
ax + by = e,
cx + dy = f

Формат ввода
Вводятся 6 вещественных чисел - коэффициенты уравнений.

Формат вывода
Вывод программы зависит от вида решения этой системы. 
Если система не имеет решений, то программа должна вывести единственное число 0. 
Если система имеет бесконечно много решений, каждое из которых имеет вид y=kx+b, то программа должна вывести число 1, а затем значения k и b. 
Если система имеет единственное решение (x0,y0), то программа должна вывести число 2, а затем значения x0 и y0. 
Если система имеет бесконечно много решений вида x=x0, y — любое, то программа должна вывести число 3, а затем значение x0. 
Если система имеет бесконечно много решений вида y=y0, x — любое, то программа должна вывести число 4, а затем значение y0. 
Если любая пара чисел (x,y) является решением, то программа должна вывести число 5.

Числа x0 и y0 будут проверяться с точностью до пяти знаков после точки. 
'''
def isclose(a, b, abs_tol=1e-06):
    return abs(a-b) <= abs_tol

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

#(a b | e)    (1 b/a | e/a)    (1 b/a | e/a)
#(c d | f) -> (1 d/c | f/c) -> (1 d/c | f/c)

# нормализуем 1 ур.
if a!=0:
    b = b/a; e = e/a; a = 1
else:
    if b!=0:
        e = e/b; b = 1

# нормализуем 2 ур.
if c!=0:
    d = d/c; f = f/c; c = 1
else:
    if d!=0:
        f = f/d; d = 1

while True:
    if a==0:
        if isclose(c,1): #a==0, c==1
            a, c = c, a
            b, d = d, b
            e, f = f, e
            #a==1, c==0
            continue
        else:                          #a==0, c==0
            if b==0:
                if isclose(d,1):
                    b, d = d, b
                    e, f = f, e
                    continue
                else:
                    if e==0 and f==0:
                        print(5)
                        break
                    else:
                        print(0)
                        break
            else:                      #a==0, c==0, b==1
                if d==1:
                    if isclose(e,f):
                        print(4, e) #or print(4,f)
                        break
                    else:
                        print(0)
                        break
                else:
                    if f==0:
                        print(4,e)
                        break
                    else:
                        print(0)
                        break
    else: #a==1
        if c==0:
            if d==0:
                if f!=0:
                    print(0)
                    break
                else:
                    if b!=0:
                        print(1, -1/b, e/b)
                        break
                    else:
                        print(3, e)
                        break
            else: #d==1
                e = e - b*f
                b = 0
                print(2, e, f)
                break
        else: #a==1,c==1
            c = 0
            d = d - b
            f = f - e
            if d!=0:
                f = f / d; d=1
            continue
