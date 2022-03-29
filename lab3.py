text = input("Введите строку: ")
max_stars = 0
b = 0
print(len(text))
for i in range(len(text) - 1):
    if text[i] == "*":
        b = i + 1
        count = 0
        r = ""
        while text[b] != "*" and b+1 != len(text):
            count += 1
            b += 1
            r = text[b]
        if count > max_stars and r == "*":
            max_stars = count
print(max_stars)
t = "l"
print("Наибольшая подстрока:", max_stars)
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
