from random import random, randrange


def ver_1(num: int) -> list[float]:
    """ Написать функцию, которая принимает целое число и с
    помощью генераторного выражения создает и возвращает новый список
    случайных чисел с длиной входящего числа.
    """
    def generate_random_values(number_val):
        for ind in range(number_val):
            yield random()

    generator = generate_random_values(num)
    return [rand_val for rand_val in generator]


def ver_2(x: int, a: int, b: int) -> list[int]:
    """Написать функцию, которая принимает три целых числа x, a, b и 
    с помощью генераторного выражения создает и возвращает 
    новый список длинной x случайных чисел от a до b. 
    Для решения данного задания рекомендуется использовать 
    функцию random.randint()."""
    def generate_random_values(number_val):
        for ind in range(number_val):
            yield randrange(a, b)

    generator = generate_random_values(x)
    return [rand_val for rand_val in generator]


def ver_3(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из n элементов, и с помощью генераторного
    выражения создает и возвращает список, элементами которого
    являются удвоенные элементы входящего списка."""
    def multiply_by_2(list1):
        for ind in list1:
            yield ind * 2

    generator = multiply_by_2(list1)
    return [value for value in generator]


def ver_4(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный 
    список, состоящий из n элементов, и с помощью генераторного 
    выражения создает и возвращает список, содержащий только 
    четные элементы входящего списка."""
    def return_even(list1):
        for ind in list1:
            if ind % 2 == 0:
                yield ind * 2

    generator = return_even(list1)
    return [value for value in generator]


def ver_5(list1: list[int]) -> list[int]:
    """Написать функцию, которая принимает целочисленный 
    список, состоящий из n элементов, и с помощью генераторного 
    выражения создает и возвращает список, содержащий только 
    положительный элементы входящего списка."""



def ver_6():
    """Написать функцию, которая принимает словарь и с помощью 
    генераторного выражения создает и возвращает новый 
    список, содержащий значения ключей входящего словаря. """


def ver_7():
    """Написать функцию, которая принимает два одинаковых по длине
    списка и с помощью генераторного выражения 
    создает и возвращает новый словарь, в котором ключами 
    являются элементы первого списка, а значениями ключей – элементы второго."""

def ver_8():
    """Написать функцию, которая принимает список и с 
    помощью генераторного выражения создает и возвращает 
    словарь, где в качестве ключей будут номера позиций элементов 
    входящего словаря, а значениями – сами элементы."""

def ver_9():
    """Написать функцию, которая принимает целочисленный 
    список, состоящий из n элементов, и с помощью генераторного 
    выражения создает новый массив элементов из тех элементов 
    входящего массива, квадрат числа которых не превышает 30."""


def ver_10():
    """Написать функцию, которая принимает список, состоящий из n элементов,
    и целое число x и с помощью генераторной функции выводит на консоль
    только те элементы входящего списка, которые больше числа x."""

def ver_11():
    """Написать функцию, которая принимает список, состоящий из n элементов,
    и два целых числа a и b и с помощью генераторной 
    функции выводит на консоль элементы входящего 
    списка от a до b включительно. Требуется предусмотреть
    ситуацию, когда значения a или b больше длины списка."""

def ver_12():
    """Написать функцию, которая принимает список списков 
    и с помощью генераторного выражения создает и возвращает 
    новый список, который содержит все элементы входящих 
    списков."""

def ver_13():
    """Написать функцию, которая принимает список и с 
    помощью генераторного выражения создает и возвращает новый 
    список, содержащий только уникальные элементы входящего 
    списка."""

def ver_14():
    """Написать функцию, которая принимает список словарей и с помощью
    генераторного выражения создает и возвращает новый словарь, который
    содержит все элементы входящих словарей. Ключи в словарях уникальны."""

def ver_15():
    """Написать функцию, которая принимает строку и с помощью
    генераторного выражения создает список, в котором
    все символы входящей строки смещены на один символ вправо
    по алфавиту, кроме символов от «ы» до «я». Требуется вернуть
    строку из созданного списка."""


if __name__ == '__main__':
    print(ver_1(15))
    print(ver_2(15, 0, 100))
    print(ver_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(ver_4([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))