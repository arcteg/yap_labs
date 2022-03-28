with open('file.txt', 'r') as f:
    text = f.read().lower().rstrip()

#длина файла (кол-во символов)
file_length = 0
for a in text:
    file_length += 1
print('Длина файла: ', file_length)

#количество гласных
vowels_count = 0
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'b']
for b in text:
    if b in vowels:
        vowels_count += 1
print('Количество гласных: ', vowels_count)

#самая частая буква
letters = {}
for letter in text:
    try:
        letters[letter] += 1
    except KeyError:
        letters[letter] = 1
most_commons = sorted(letters.items(), key=lambda kv: kv[1], reverse=True)
most_freq = most_commons[0]
print('Самая часто употребляемая буква: ', most_freq[0])

#количество строк
l = 0
for line in open('file.txt', 'r'):
    l += 1
print('Количество строк: ', l)
f.close()