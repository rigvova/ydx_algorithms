"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество таких элементов. 
"""
n = int(input())
ranges = list(map(int, input().split(" ")))


def find_vasya(ranges):
    vas_i = []
    vas_scores = []

    for i in range(1, len(li)-1):
        cur = li[i]
        if str(cur)[-1]==5:
            if l[i+1] < cur:
                vas_li.append(i)

    srt = sorted(ranges)

    max = 0
    for i in sorted(vas_li):
        if ranges[i-1] == srt[0]:
            pass
    
    return cnter


print(find_vasya(ranges))
