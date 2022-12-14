def version_1(int_list: list[int]) -> bool:
    """1. Написать функцию, которая принимает целочисленный
    список с количеством элементов 1 или более и возвращает
    True, если цифра 6 является первым или последним элементом
    списка."""
    if int_list[0] == 6 or int_list[-1] == 6:
        return True
    else:
        return False


def version_2(int_list1: list[int], int_list2: list[int]) -> bool:
    """Написать функцию, которая принимает два
    целочиcленных списка и возвращает True, если
    первые или последние элементы данных списков
    равны. Оба списка содержат 1 или более элементов."""
    if int_list1[0] == int_list2[0] or int_list1[-1] == int_list2[-1]:
        return True
    else:
        return False


def version_3(int_list: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из трех элементов, и возвращает новый
    перевернутый список. Например, на входе {1,2,3}, а на выходе
    {3,2,1}."""
    reversed_list = []
    for i in range(len(int_list) - 1, -1, -1):
        reversed_list.append(int_list[i])
    return reversed_list


def version_4(int_list1: list[int], int_list2: list[int]) -> list[int]:
    """Написать функцию, которая принимает два целочисленных списка,
    содержащих по три элемента каждый, и возвращает новый список,
    состоящий из двух элементов, являющихся средними во входящих списках.
    Например, для следующих входящих списков {1,2,3} и {3,4,5} итоговым будет {2,4}."""
    int_list1.remove(max(int_list1))
    int_list2.remove(max(int_list2))
    int_list1.remove(min(int_list1))
    int_list2.remove(min(int_list2))
    return [int_list1[0], int_list2[0]]


def version_5(list1: list[int]) -> bool:
    """Написать функцию, которая принимает целочисленный
    список и возвращает True, если длина списка больше нуля и
    первый и последний элемент списка равны."""
    if len(list1) != 0 and list1[0] == list1[-1]:
        return True
    else:
        return False


def version_6(list1: list[int]) -> int:
    """Написать функцию, которая принимает целочисленный
    список, содержащий три элемента, и возвращает сумму этих
    элементов."""
    summ = 0
    for i in list1:
        summ = summ + i
    return summ


def version_7(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный
    список, содержащий три элемента, и изменяет данный список
    путем изменения всех его элементов на максимальный крайний
    элемент списка. Например, для входящего списка {1,2,3} изменённым будет {3,3,3}."""
    max_el = list1[0]
    if max_el < list1[-1]:
        max_el = list1[-1]
    for i in range(len(list1)):
        list1[i] = max_el
    return list1


def version_8(list1: list[int]) -> bool:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из n элементов, и возвращает True, если он
    содержит числа 2 или 3."""
    for iterator in list1:
        if iterator == 2 or iterator == 3:
            return True
    return False


def version_9(list1: list[int]) -> int:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из n элементов, и возвращает количество
    четных чисел в списке."""
    num_of_even = 0
    for iterator in list1:
        if iterator % 2 == 0:
            num_of_even += 1
    return num_of_even


def version_10(list1: list[int]) -> int:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из n элементов, и возвращает сумму элементов списка.
     Однако стоит исключить из подсчета число 13 и
    числа, которые следуют после него. Например, для входящего
    списка {1,2,3,13,4} сумма будет равна 6."""
    summ = 0
    for i in range(len(list1)):
        if list1[i] == 13:
            return summ
        else:
            summ += list1[i]
    return summ


def version_11(list1: list[int]) -> bool:
    """Написать функцию, которая принимает целочисленный список,
     состоящий из n элементов, и возвращает True, если
    в каком-то месте списка по порядку содержатся элементы 1,2,3
    или комбинации их перестановок."""
    string1 = ''
    for i in list1:
        string1 += str(i)
    if '123' in string1:
        return True
    if '132' in string1:
        return True
    if '213' in string1:
        return True
    if '231' in string1:
        return True
    if '321' in string1:
        return True
    if '312' in string1:
        return True
    return False


def version_12(dict1: dict, dict2: dict) -> dict:
    """Написать функцию, которая принимает два словаря и
    возвращает новый словарь, в котором значения одинаковых
    ключей из входящих словарей являются суммой, а разные ключи
    просто добавляются в новый словарь. Например, для входящих
    словарей {‘a’:200, ‘b’:50} и {‘a’:100, ‘c’:500} выходным
    словарем будет {‘a': 300, ‘b’:50, ‘c’:500}."""
    res_dict = {}
    for key in dict1.keys():
        if key in dict2:
            res_dict.update({key: dict1.get(key) + dict2.get(key)})
        else:
            res_dict.update({key: dict1.get(key)})
    for key in dict2.keys():
        if key not in res_dict.keys():
            res_dict.update({key: dict2.get(key)})
    return res_dict


def version_13(list1: list, list2: list) -> dict or str:
    """Написать функцию, которая принимает два списка и
    возвращает словарь, в котором ключами выступают элементы
    первого списка, а значениями ключей – элементы второго.
    Требуется предусмотреть ситуации, когда один из списков или оба
    будут пустыми. В ситуации, когда один список по длине больше
    другого, последние элементы большего по длине списка, не учитывать."""
    min_len = len(list1)
    if min_len > len(list2):
        min_len = len(list2)
    res_dict = {}
    if len(list1) == 0 and len(list2) == 0:
        return 'Массивы пусты'
    elif len(list1) == 0:
        return "Первый массив пустой"
    elif len(list2) == 0:
        return "Второй массив пустой"
    else:
        for i in range(min_len):
            res_dict.update({list1[i]: list2[i]})
        return res_dict


def version_14(list1: list[dict[{bool: str}]]) -> list[str]:
    """Написать функцию, которая принимает список, состоящий из n словарей,
     где в каждом словаре присутствуют ключи
    status (True или False) и name (строка). Вернуть список,
     который будет содержать все значения ключей name в тех словарях,
    где значение status является True. В случае отсутствия таковых
    вернуть пустой список."""
    return_list = []
    for dictionary in list1:
        return_list.append(dictionary.get(True))
    return return_list


def version_15(list1: list) -> dict:
    """Написать функцию, которая принимает на вход список,
    состоящий из n различных элементов. Вернуть словарь,
    в котором ключами являются элементы входящего списка,
    а их значениями – число повторений этих элементов во входящем
    списке."""
    result_dict = {}
    values = []
    for i in range(len(list1)):
        if not list1[i] in values:
            values.append(list1[i])

    for i in range(len(values)):
        count = 0
        for j in list1:
            if values[i] == j:
                count += 1
        result_dict.update({values[i]: count})

    return result_dict


print("Вариант 1")
print(version_1([1, 2, 3]))
print("Вариант 2")
print(version_2([1, 2, 3], [1, 2, 3]))
print("Вариант 3")
print(version_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print("Вариант 4")
print(version_4([1, 2, 3], [1, 2, 3]))
print("Вариант 5")
print(version_5([1, 2, 3]))
print("Вариант 6")
print(version_6([1, 2, 3]))
print("Вариант 7")
print(version_7([1, 2, 3]))
print("Вариант 8")
print(version_8([1, 1, 4]))
print("Вариант 9")
print(version_9([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print("Вариант 10")
print(version_10([1, 1, 2, 13, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print("Вариант 11")
print(version_11([3, 2, 1, 4, 5, 6, 7, 8, 9]))
print("Вариант 12")
print(version_12({"a": 200, "b": 50}, {"a": 100, "c": 500}))
print("Вариант 13")
print(version_13([1, 2, 3], [1]))
print("Вариант 14")
print(version_14([{True: 'cat', False: 'dog'}, {True: 'rabbit', False: 'horse'}]))
print("Вариант 15")
print(version_15(['1', 1, '1', 6, 6, 4, 'd', 'b', 'n', 5, 'd', 'a', '1', 'f', 4, 4, 6, 5, 'a', 4, 4, 'f']))
