"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки. Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу. 
"""
with open('input.txt', 'r') as f:
    text = f.readlines()
text = ' '.join(text).replace('\n', '')

d = {}
counts = []
for word in filter(lambda x: x!='', text.split(' ')):
    if d.get(word, None) is None:
        d[word] = 0
        counts.append(0)
    else:
        d[word] += 1
        counts.append(d[word])

print(' '.join(map(str, counts)))
