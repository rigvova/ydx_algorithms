"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. 
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу. 
"""
with open('input.txt', 'r') as f:
    text = f.readlines()
text = ' '.join(text).replace('\n', '')

d = {}
mx = 0
for word in filter(lambda x: x!='', text.split(' ')):
    if d.get(word, None) is None:
        d[word] = 0
    d[word] += 1
    if d[word]>mx:
        mx=d[word]

new_li = []
for x in d:
    if d[x]==mx:
        new_li.append(x)

print(min(new_li))
