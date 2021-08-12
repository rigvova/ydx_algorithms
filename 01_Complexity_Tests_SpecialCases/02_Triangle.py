'''
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами. Если это возможно, выведите строку YES, иначе выведите строку NO.
Треугольник — это три точки, не лежащие на одной прямой.
'''
a = int(input())
b = int(input())
c = int(input())

arglist = (a,b,c)

mx = max(arglist)
sides_sum = a+b+c

if min(arglist) <= 0:
    print('NO')
elif (mx >= sides_sum - mx):
    print('NO')
else:
    print('YES')