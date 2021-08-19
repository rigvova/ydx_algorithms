"""
В данном списке из n ≤ 10^5 целых чисел найдите три числа,произведение которых максимально.
Решение должно иметь сложность O(n), где n - размер списка.
Выведите три искомых числа в любом порядке. 
"""
li = list(map(int, input().split()))

max1=li[0]
max2=None
max3=None
min1=li[0]
min2=None
min3=None

if li[1] >= max1:
    max2=max1
    max1=li[1]
    min2=li[1]
else:
    max2=li[1]
    min2=min1
    min1=li[1]

if li[2] >= max1:
    max3=max2
    max2=max1
    max1=li[2]
    min3=li[2]
elif li[2] >= max2:
    max3=max2
    max2=li[2]
    min3=min2
    min2=li[2]
else:
    max3=li[2]
    min3=min2
    min2=min1
    min1=li[2]

for x in li[3:]:
    if x >= max1:
        max3=max2; max2=max1; max1=x
    elif x >= max2:
        max3=max2; max2=x
    elif x > max3:
        max3=x
    elif x <= min1:
        min3=min2; min2=min1; min1=x
    elif x <= min2:
        min3=min2; min2=x
    elif x < min3:
        min3=x

if (min1*min2*max1) >= (max1*max2*max3):
    print(min1, min2, max1)
else:
    print(max1, max2, max3)