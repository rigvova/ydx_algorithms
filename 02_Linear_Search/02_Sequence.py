
"""
По последовательности чисел во входных данных определите ее вид:

    CONSTANT – последовательность состоит из одинаковых значений
    ASCENDING – последовательность является строго возрастающей
    WEAKLY ASCENDING – последовательность является нестрого возрастающей
    DESCENDING – последовательность является строго убывающей
    WEAKLY DESCENDING – последовательность является нестрого убывающей
    RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

Признаком окончания последовательности является число -2×10^9. 
Оно в последовательность не входит. 
"""

li = []
flag = True
while flag:
    temp = float(input())
    if temp == -2000000000:
        flag = False
    else:
        li.append(temp)


def findcase(li):
    if len(li) == 0:
        return 'RANDOM'
    elif len(li) == 1:
        return 'CONSTANT'

    asc_flag = True
    wasc_flag = True
    desc_flag = True
    wdesc_flag = True
    for i in range(1, len(li)):
        prev = li[i-1]
        cur = li[i]
        if cur < prev:
            asc_flag = False
            wasc_flag = False
        if cur <= prev:
            asc_flag = False
        if cur > prev:
            desc_flag = False
            wdesc_flag = False
        if cur >= prev:
            desc_flag = False


    if asc_flag:
        return "ASCENDING"
    elif desc_flag:
        return "DESCENDING"

    if wdesc_flag & wasc_flag:
        return "CONSTANT"
    elif wdesc_flag:
        return "WEAKLY DESCENDING"
    elif wasc_flag:
        return "WEAKLY ASCENDING"
    else:
        return "RANDOM"


print(findcase(li))
