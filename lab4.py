with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower().strip()
    text = text.replace('\n', '') and text.replace(' ', '')
output = open('output.txt', 'w', encoding='utf-8')

#  длина файла (кол-во символов)
file_length = 0
for a in text:
    if a != ' ' and a != '\n':
        file_length += 1
file_length = 'Длина файла: ' + str(file_length) + '\n'
output.write(file_length)

#  количество гласных
count = 0
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for b in text:
    if b != ' ' and b != '\n':
        if b in vowels:
            count += 1
vowels_count = 'Количество гласных: ' + str(count) + '\n'
output.write(vowels_count)

#  самая частая буква
i = max = maxl = 0
c = ''
for i in text:
    if text.count(i) > max and i not in c:
        max = text.count(i)
        maxl = i
        c += i
max_vowel = 'Самая часто употребляемая буква (' + str(maxl) + '): ' + str(max) + '\n'
output.write(max_vowel)


#  количество строк
l = 0
for line in open('input.txt', 'r'):
    l += 1
string_count = 'Количество строк: ' + str(l)
output.write(string_count)
output.close()
