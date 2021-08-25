"""
Широко известна следующая задача для младших школьников. Три черепахи ползут по дороге.
Одна черепаха говорит: “Впереди меня две черепахи”. Другая черепаха говорит: “Позади меня две черепахи”.
Третья черепаха говорит: “Впереди меня две черепахи и позади меня две черепахи”.
Как такое может быть? Ответ: третья черепаха врет! По дороге одна за другой движутся N черепах.
Каждая черепаха говорит фразу вида: “Впереди меня ai черепах, а позади меня bi черепах”.
Ваша задача определить, сколько самое большее количество черепах могут говорить правду.

Формат ввода
В первой строке вводится целое число N (1 ≤ N ≤ 10000) строк,
содержащих целые числа ai и bi, по модулю не превосходящие 10000, описывающие высказывание i-ой черепахи.

Формат вывода
Выведите целое число M – максимальное количество черепах, которые могут говорить
"""
g1 = {}
g2 = {}
tmp = list(input())
for i in range(1, len(tmp)):
    g1[tmp[i-1]+tmp[i]] = g1.get(tmp[i-1]+tmp[i], 0) + 1
tmp = list(input())
for i in range(1, len(tmp)):
    g2[tmp[i-1]+tmp[i]] = g2.get(tmp[i-1]+tmp[i], 0) + 1

diff = set(g1).intersection(set(g2))
closeness = 0
for gene in diff:
    closeness += g1[gene]

print(closeness)