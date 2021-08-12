""".
Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""

try:
    li = list(map(int, input().split(" ")))
except:
    li = []


def isrising(li):
    if len(li) == 0:
        return False
    elif len(li) == 1:
        return True

    rise_flag = True
    for i in range(1, len(li)):
        prev = li[i-1]
        cur = li[i]
        if cur <= prev:
            rise_flag = False

    return rise_flag


if isrising(li):
    print('YES')
else:
    print('NO')
