with open('file.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower().rstrip()
    text = text.replace('\n', '') and text.replace(' ', '')
output = open('output.txt', 'w', encoding='utf-8')

#длина файла (кол-во символов)
file_length = 0
for a in text:
    file_length += 1
file_length = 'Длина файла: ' + str(file_length) + '\n'
output.write(file_length)

#  количество гласных
count = 1
vowels = ['a', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for b in text:
    if b in vowels:
        count += 1
vowels_count = 'Количество гласных: ' + str(count) + '\n'
output.write(vowels_count)

#  самая частая буква
i = max = maxw = 0
c = ''
for i in range(len(text)):
    if text.count(text[i]) > max and text[i] not in c:
        max = text.count(text[i])
        maxw = text[i]
        c += text[i]
max_vowel = 'Самая часто употребляемая буква (' + str(maxw) + '): ' + str(max) + '\n'
output.write(max_vowel)


#  количество строк
l = 0
for line in open('file.txt', 'r'):
    l += 1
string_count = 'Количество строк: ' + str(l)
output.write(string_count)
output.close()
