"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу. 

В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива. 
Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
В третьей строке вводится одно целое число x, не превосходящее по модулю 1000. 
"""
le = int(input())
li = list(map(int, input().split(" ")))
a = int(input())


def findclose(li, a):
    if len(li) == 0:
        return None
    elif len(li) == 1:
        return li[0]

    closest = li[0]
    dist = abs(a - closest)
    for x in li[1:]:
        newdist = abs(a-x)
        if newdist < dist:
            dist = newdist
            closest = x
    return closest


print(findclose(li, a))
