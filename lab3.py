text = input("Введите строку: ")
s = text.split('*')
max_word = str(len(max(s, key=len)))
max_string = max(s, key=len)
print("Наибольшая подстрока: " + max_string)
print("Длина наибольшей подстроки: " + max_word)
t = "l"
for i in range(len(text)):
    if text[i] == "*":
        print(text[i], end="")
    else:
        if t == "l":
            print(text[i].upper(), end="")
            t = "u"
        else:
            print(text[i].lower(), end="")
            t = "l"