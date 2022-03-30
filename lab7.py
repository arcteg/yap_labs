dictionary = {"Computer": "Компьютер",
              "Keyboard": "Клавиатура",
              "Can": ["Мочь", "Банка"],
              "Earth": "Земля",
              "Sun": "Солнце",
              "Air": "Воздух",
              "Box": "Ящик",
              "Fire": "Огонь",
              "Right": ["Право", "Прав"],
              "Pen": "Ручка"
              }
print(dictionary)


#  добавление пары
def add_pair(eng, rus):
    dictionary[eng] = rus
add_pair('Put', ["Ставить", "помещать"])
print(dictionary)


#  удаление
def del_pair(word):
    if word in dictionary.keys():
        del dictionary[word]
del_pair("Can")
print(dictionary)


#  проверка на вхождение
def check_pair(word):
    if word in dictionary or word in dictionary.values():
        return True
    else:
        return False
print(check_pair("Земля"))


#  вывод англ слов короче 5 символов
def prnt_wrds():
    for i in dictionary.keys():
        if len(i) < 5:
            print(i)
prnt_wrds()


#  очистка словаря
def clear_dict():
    dictionary.clear()
#  в самом конце

#  сортировка словаря
def sort_dict(dt):
    dictionary = dict(sorted(dt.items()))
    return dictionary
print(sort_dict(dictionary))


#  вывод всего словаря
def prnt_dctnry(dict):
    for i in dict:
        print(i, dict[i])
    #  print(dictionary)
prnt_dctnry(dictionary)


#  изменение пары
def chng_pair(old_key):
    new_key = input("Введите новый ключ: ")
    new_value = input("Введите новое значение: ").split()
    dictionary[new_key] = dictionary.pop(old_key)
    dictionary[new_key] = new_value
chng_pair("Sun")
print(dictionary)


# смена ключа и значения местами
def reverse(key):
    dictionary[dictionary.pop(key)] = key
reverse("Air")
print(dictionary)

clear_dict()
print(dictionary)