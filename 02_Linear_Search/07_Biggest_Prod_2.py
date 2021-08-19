"""
Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально. 
Выведите эти числа в порядке неубывания.
Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.
Решение должно иметь сложность O(n), где n - размер списка. 
"""
li = list(map(int, input().split()))

max1=None
max2=None
min1=None
min2=None

if li[1] >= li[0]:
    max1=li[1]
    max2=li[0]
    min1=li[0]
    min2=li[1]
else:
    max1=li[0]
    max2=li[1]
    min1=li[1]
    min2=li[0]

for x in li[2:]:
    if x >= max1:
        max2=max1; max1=x
    elif x > max2:
        max2=x
    elif x <= min1:
        min2=min1; min1=x
    elif x < min2:
        min2=x

if (min1*min2) >= (max1*max2):
    print(min1, min2)
else:
    print(max2, max1)