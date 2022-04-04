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


#  добавление пары
def add_pair(eng, rus):
    rus = rus.replace(',', '').split()
    if len(rus) == 1:
        rus = str(rus)
    dictionary.update({eng: rus})


#  удаление
def del_pair(rm_key):
    if rm_key in dictionary.keys():
        del dictionary[rm_key]


#  проверка на вхождение
def check_pair(key):
    if key.lower().capitalize() in dictionary or key in dictionary.values():
        return 'Слово ' + key + ' находится в словаре'
    else:
        return 'Слово ' + key + ' отсутствует в словаре'


#  вывод англ слов короче 5 символов
def prnt_wrds():
    for i in dictionary.keys():
        if len(i) < 5:
            print(i)


#  очистка словаря
def clear_dict():
    dictionary.clear()


#  сортировка словаря
def sort_dict(dt):
    dictionary = dict(sorted(dt.items()))
    return dictionary


#  вывод всего словаря
def prnt_dctnry(dict):
    for i in dict:
        print(i, dict[i])
    #  print(dictionary)


#  изменение пары
def chng_pair(old_key):
    new_key = input("Введите новый ключ: ")
    new_value = input("Введите новое значение: ").split()
    dictionary[new_key] = dictionary.pop(old_key)
    dictionary[new_key] = new_value


# смена ключа и значения местами
def reverse(rkey):
    if rkey == 'all':
        result = {}
        for key, value in dictionary.items():
            if isinstance(value, list):
                for item in value:
                    result[item] = key
            else:
                result[value] = key
        return result
    else:
        dictionary[dictionary.pop(rkey)] = rkey
    print(dictionary)

####################################################
####################ТЕСТИРОВАНИЕ####################
####################################################

num = 1
while num:
    num = input("""
    \r0)Выход из программы
    \r1)Добавление пары
    \r2)Удаление пары
    \r3)Проверка пары на вхождение
    \r4)Вывод слов на английском короче 5 символов
    \r5)Очистка словаря
    \r6)Сортировка словаря
    \r7)Вывод всего словаря
    \r8)Изменеие пары
    \r9)Смена ключа и значения местами
    \rВыберите операцию (0-9): """)

    if num == '1':
        eng = input('Введите ключ: ')
        rus = input('Введите значение(я) через запятую(ые): ')
        add_pair(eng, rus)
        print(dictionary)
    elif num == '2':
        rm_key = input('Введите ключ для удаления: ')
        del_pair(rm_key)
        print(dictionary)
    elif num == '3':
        key = input('Введите ключ для проверки: ')
        print(check_pair(key))
    elif num == '4':
        prnt_wrds()
    elif num == '5':
        clear_dict()
        print(dictionary)
    elif num == '6':
        print(sort_dict(dictionary))
    elif num == '7':
        prnt_dctnry(dictionary)
    elif num == '8':
        old_key = input('Введите старый ключ: ')
        chng_pair(old_key)
        print(dictionary)
    elif num == '9':
        rkey = input('Введите ключ или all: ')
        print(reverse(rkey))
    elif num == '0':
        print('Програма завершена!')
        break
    else:
        print('Вы ввели недопустимое значение, попробуйте ещё раз.')
