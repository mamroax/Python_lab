def version_1(int_num: int) -> list[int]:
    """Написать функцию, которая принимает целое число и
    возвращает сгенерированный список, содержащий количество
    элементов от 0 до входящего числа включительно."""
    return [i for i in range(0, int_num)]


def version_2(list1: list[str]) -> None:
    """Написать функцию, которая принимает список, который
    содержит строки и выводит на экран новые списки из входящих строк."""
    [print([list1[i]]) for i in range(len(list1))]


def version_3(list1: list) -> None:
    """Написать функцию, которая принимает список и выводит
    в консоль значения списка через точку с запятой. Требуется
    решить задачу одной строкой с использованием списка с оператором «*»."""
    [print(i, end=';') for i in list1]


def version_4(list1: list) -> sum:
    """Написать функцию, которая принимает список, состоящий
    из n элементов, и возвращает их сумму."""
    summ = 0
    for i in list1:
        summ += i
    return summ


def version_5(list1: [str]) -> sum:
    """Написать функцию, которая принимает список, состоящий
    из строк, которые являются целочисленными значениями
    или значениями с плавающей точкой, и возвращает их сумму"""
    summ = 0
    for i in list1:
        summ += float(i)
    return summ


def version_6(list1: list) -> tuple[int, int]:
    """Написать функцию, которая принимает список, состоящий
    из n элементов, и возвращает количество целых чисел и
    чисел с плавающей точкой"""
    num_of_int = 0
    num_of_float = 0
    for i in list1:
        if type(i) == int:
            num_of_int += 1
        elif type(i) == float:
            num_of_float += 1
    return num_of_int, num_of_float


def version_7(list1: list[int]) -> None:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из n элементов, и записывает в файл новый
    список, состоящий из тех элементов входящего списка,
    значения квадрата которых не превышают 30"""
    try:
        res_str = ''
        for iterator in list1:
            if iterator * iterator > 30:
                break
            else:
                res_str += str(iterator) + ' '
        my_file = open("list.txt", "w+")
        my_file.write(res_str)
    except Exception:
        print('Error massage')
    finally:
        my_file.close()
        print('Текстовый файл создан и заполнен')


def version_8(list1: list[int]) -> list[list[int]]:
    """Написать функцию, которая принимает целочисленный
    список, состоящий из n элементов, и возвращает список, состоящий
    из новых списков, элементами которых являются числа
    от 0 до значений элемента во входящем списке включительно.
    Например, входящий список имеет вид [1,2,3] на выходе будет
    список списков [[0,1], [0,1,2], [0,1,2,3]]"""
    res_list = []
    for iterator in list1:
        res_list.append([i for i in range(iterator + 1)])
    return res_list


def version_9(list1: list[int], num: int) -> None:
    """Написать функцию, которая принимает целочисленный
    список, содержащий n элементов, и целое число, и выводит на
    экран сгенерированные списки, содержащие n элементов с шагом
    итерации, равном элементу входящего списка"""
    for iterator in list1:
        print([jiterator for jiterator in range(0, iterator * num, iterator)])


def version_10(string1: str, string2: str) -> int:
    """Написать функцию, которая принимает на вход две
    разных строки и возвращает количество совпадений двух символов
    в строках. Например, на входе две строки «xadasw» и
    «xad» совпадением будет считаться группа символов «xa» и «ad»"""
    first = 0
    second = 2
    counter = 0
    for i in range(len(string1) - 1):
        if string1[first:second] in string2:
            # print(string1[first:second])
            counter += 1
        first += 1
        second += 1
    return counter


print('Вариант 1')
print(version_1(100))
print('Вариант 2')
version_2(['string', 'string', 'string', 'string', 'string', 'string'])
print('Вариант 3')
version_3(['1', 2, 'string', 3, 'dog', '9'])
print()
print('Вариант 4')
print('Сумма чисел ', version_4([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('Вариант 5')
print('Сумма чисел ', version_5(['12', '2.3', '123.23', '-100', '-12.4', '67']))
print('Вариант 6')
print('Количество целых', version_6([12, 2.3, 123.23, -100, -12.4, 67, 7])[0], 'вещественных',
      version_6([12, 2.3, 123.23, -100, -12.4, 67, 7])[1])
print('Вариант 7')
version_7([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print('Вариант 8')
print(version_8([1, 2, 3, 4, 5]))
print('Вариант 9')
version_9([1, 2, 3, 4, 5, -6], 6)
print('Вариант 10')
print(version_10('xadasw', 'xad'))
