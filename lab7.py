dictionary = {"Компьютер": "Computer",
              "Клавиатура": "Keyboard",
              "Наушники": "Headphones",
              "Земля": "Earth",
              "Солнце": "Sun",
              "Воздух": "Air",
              "Вода": "Water",
              "Огонь": "Fire",
              "Окно": "Window",
              "Ручка": "Pen"
              }


#  добавление пары
def add_pair(rus, eng):
    dictionary[rus] = eng


#  удаление
def del_pair(rus):
    del dictionary[rus]


#  проверка на вхождение
def check_pair(word):
    if word in dictionary:
        return True
    else:
        return False


#  вывод англ слов короче 5 символов
def prnt_wrds():
    for i in dictionary.values():
        if len(i) < 5:
            print(i)


#  очистка словаря
def clear_dict():
    dictionary.clear()


#  сортировка словаря
def sort_dict():
    sorted_dict = sorted(dictionary.items())
    return sorted_dict


#  вывод всего словаря
def prnt_dctnry():
    print(dictionary)


#  изменение пары
def chng_pair(old_key):
    old_value = dictionary.get(old_key)
    rus = list(dictionary.keys())
    eng = list(dictionary.values())
    old_key_index = rus.index(old_key)
    old_value_index = eng.index(old_value)
    new_key = input("Введите новый ключ: ")
    new_value = input("Введите новое значение: ")
    rus[old_key_index] = new_key
    eng[old_value_index] = new_value
    d = dict(zip(rus, eng))


# смена ключа и значения местами
def reverse(key):
    dictionary[dictionary.pop(key)] = key
