a = "абвгдекааюсаб"
b = "аеёиоуыэюябвгджзйклмнпрстфхцчшщ"
c = ""
i = max = maxw = 0
for i in range(len(a)):
    if a.count(a[i]) > max and a[i] not in c:
        max = a.count(a[i])
        maxw = a[i]
        c += a[i]
print(f"Максимальное {maxw} = {max}")
