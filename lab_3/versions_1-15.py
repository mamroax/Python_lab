from random import random, randrange, randint


def generate_random_values_range(number_val, a, b):
    for ind in range(number_val):
        yield randrange(a, b)


def generate_random_values(number_val):
    for ind in range(number_val):
        yield random()


def gen_multiply_by_2(list1):
    for ind in list1:
        yield ind * 2


def gen_return_even(list1):
    for ind in list1:
        if ind % 2 == 0:
            yield ind * 2


def gen_return_pos(list1: list[int]):
    for ind in list1:
        if ind >= 0:
            yield ind


def make_list(n: int) -> list[int]:
    return [randint(0, n*3) for i in range(n)]


def make_list_w_neg(n: int) -> list[int]:
    return [randint(-n*3, n*3) for i in range(n)]


def gen_return_dict_keys(dict1: dict):
    for key in dict1.keys():
        yield key


def gen_list(list1: list):
    for ind in list1:
        yield ind


def make_seq(n):
    return [i for i in range(n)]


def gen_seq(list1, a, b):
    for ind in list1:
        if ind >= a and ind <= b:
            yield ind


def gen_list_of_lists_2_list(list1):
    for ind in list1:
        for ind1 in ind:
            yield ind1


def gen_unique(list1):
    for ind in range(len(list1)):
        if list1[ind] not in list1[ind+1:]:
            yield list1[ind]


def gen_list_of_dicts(list1: list[dict]):
    for ind in list1:
        for ind1 in ind.keys():
            yield ind1
        for ind2 in ind.values():
            yield ind2


def gen_alphabet(list1: list):
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alph1 = 'ыьэюя'
    for i in list1:
        ind = alph.find(i)
        if i in alph:
            if i not in alph1:
                yield alph[ind + 1]
            else:
                yield alph[ind]



def ver_1(num: int) -> list[float]:
    """ Написать функцию, которая принимает целое число и с
    помощью генераторного выражения создает и возвращает новый список
    случайных чисел с длиной входящего числа.
    """
    generator = generate_random_values(num)
    return [rand_val for rand_val in generator]


def ver_2(x: int, a: int, b: int) -> list[int]:
    """Написать функцию, которая принимает три целых числа x, a, b и 
    с помощью генераторного выражения создает и возвращает 
    новый список длинной x случайных чисел от a до b. 
    Для решения данного задания рекомендуется использовать 
    функцию random.randint()."""
    generator = generate_random_values_range(x, a, b)
    return [rand_val for rand_val in generator]


def ver_3(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из n элементов, и с помощью генераторного
    выражения создает и возвращает список, элементами которого
    являются удвоенные элементы входящего списка."""
    generator = gen_multiply_by_2(list1)
    return [value for value in generator]


def ver_4(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный 
    список, состоящий из n элементов, и с помощью генераторного 
    выражения создает и возвращает список, содержащий только 
    четные элементы входящего списка."""
    generator = gen_return_even(list1)
    return [value for value in generator]


def ver_5(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный 
    список, состоящий из n элементов, и с помощью генераторного 
    выражения создает и возвращает список, содержащий только 
    положительный элементы входящего списка."""
    generator = gen_return_pos(list1)
    return [value for value in generator]


def ver_6(dict1: dict) -> list:
    """Написать функцию, которая принимает словарь и с помощью 
    генераторного выражения создает и возвращает новый 
    список, содержащий значения ключей входящего словаря. """
    generator = gen_return_dict_keys(dict1)
    return [value for value in generator]


def ver_7(list1: list, list2: list) -> dict:
    """Написать функцию, которая принимает два одинаковых по длине
    списка и с помощью генераторного выражения 
    создает и возвращает новый словарь, в котором ключами 
    являются элементы первого списка, а значениями ключей – элементы второго."""
    generator1 = gen_list(list1)
    generator2 = gen_list(list2)
    return dict.fromkeys([value1 for value1 in generator1], [value2 for value2 in generator2])


def ver_8(list1: list) -> dict:
    """Написать функцию, которая принимает список и с 
    помощью генераторного выражения создает и возвращает 
    словарь, где в качестве ключей будут номера позиций элементов 
    входящего словаря, а значениями – сами элементы."""
    generator = gen_list(list1)
    dict1 = {}
    count = 0
    for value in generator:
        dict1.update({count: value})
        count += 1
    return dict1


def ver_9(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный 
    список, состоящий из n элементов, и с помощью генераторного 
    выражения создает новый массив элементов из тех элементов 
    входящего массива, квадрат числа которых не превышает 30."""
    generator = gen_list(list1)
    return [value for value in generator if value*value <= 30]


def ver_10(list1: list, x: int):
    """Написать функцию, которая принимает список, состоящий из n элементов,
    и целое число x и с помощью генераторной функции выводит на консоль
    только те элементы входящего списка, которые больше числа x."""
    generator = gen_list(list1)
    return [value for value in generator if value > x]


def ver_11(list1: list, a: int, b: int):
    """Написать функцию, которая принимает список, состоящий из n элементов,
    и два целых числа a и b и с помощью генераторной 
    функции выводит на консоль элементы входящего 
    списка от a до b включительно. Требуется предусмотреть
    ситуацию, когда значения a или b больше длины списка."""
    generator = gen_seq(list1, a, b)
    return [value for value in generator]


def ver_12(list1: list[list]) -> list:
    """Написать функцию, которая принимает список списков 
    и с помощью генераторного выражения создает и возвращает 
    новый список, который содержит все элементы входящих 
    списков."""
    generator = gen_list_of_lists_2_list(list1)
    return [value for value in generator]


def ver_13(list1: list):
    """Написать функцию, которая принимает список и с 
    помощью генераторного выражения создает и возвращает новый 
    список, содержащий только уникальные элементы входящего 
    списка."""
    generator = gen_unique(list1)
    return [value for value in generator]


def ver_14(list1: list[dict]) -> dict:
    """Написать функцию, которая принимает список словарей и с помощью
    генераторного выражения создает и возвращает новый словарь, который
    содержит все элементы входящих словарей. Ключи в словарях уникальны."""
    generator = gen_list_of_dicts(list1)
    return [value for value in generator]


def ver_15(string: str):
    """Написать функцию, которая принимает строку и, с помощью
    генераторного выражения, создает список, в котором
    все символы входящей строки смещены на один символ вправо
    по алфавиту, кроме символов от «ы» до «я». Требуется вернуть
    строку из созданного списка."""
    generator = gen_alphabet(list(string))
    str1 = ''
    for value in generator:
        str1 += value
    return str1


if __name__ == '__main__':
    print('Вариант 1 ', ver_1(15))
    print('Вариант 2 ', ver_2(15, 0, 100))
    print('Вариант 3 ', ver_3(make_list(10)))
    print('Вариант 4 ', ver_4(make_list(10)))
    print('Вариант 5 ', ver_5(make_list_w_neg(10)))
    print('Вариант 6 ', ver_6({123: 'kek', 321: "mek", 'geg': 213}))
    print('Вариант 7 ', ver_7(make_list(10), make_list(10)))
    print('Вариант 8 ', ver_8(make_list(10)))
    print('Вариант 9 ', ver_9(make_list(10)))
    print('Вариант 10 ', ver_10(make_list(10), 10))
    print('Вариант 11 ', ver_11(make_seq(10), 2, 7))
    print('Вариант 12 ', ver_12([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]))
    print('Вариант 13 ', ver_13([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,6]))
    print('Вариант 14 ', ver_14([{1: 'edw', 2: 'dfe', 3: 'sdce'},{4: 'wddf', 5:'dwcf', 6:'dsdfsd'}]))
    print('Вариант 15 ', ver_15('екрнуцыупйцунгцгкуелячсячупкпукмавьбтьзэщдортьысч'))