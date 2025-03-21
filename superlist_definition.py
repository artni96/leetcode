def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    if len(list_set_1) == len(list_set_2):
        count = 0
        for elem in range(len(list_set_1)):
            if list_set_1[elem] in list_set_2:
                count += 1
        if count == len(list_set_1) == len(list_set_2):
            return 'Наборы равны.'
    elif len(list_set_1) > len(list_set_2):
        count = 0
        for elem in range(len(list_set_2)):
            if list_set_2[elem] in list_set_1:
                count += 1
        if count == len(list_set_2):
            return f'Набор {list_set_1} - супермножество.'
    elif len(list_set_2) > len(list_set_1):
        count = 0
        for elem in range(len(list_set_1)):
            if list_set_1[elem] in list_set_2:
                count += 1
        if count == len(list_set_1):
            return f'Набор {list_set_2} - супермножество.'
    return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))