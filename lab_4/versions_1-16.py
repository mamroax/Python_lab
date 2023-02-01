import os
from datetime import datetime, timedelta
from time import gmtime, strftime


def var1(today: datetime) -> bool:
    """1. Написать функцию, которая принимает объект datetime
    и возвращает True, если год полученного значения високосный."""
    if today.year % 4 == 0 and today.year % 100 != 0 or today.year % 400 == 0:
        return True
    else:
        return False


def var2(stroka: str) -> datetime:
    """2. Написать функцию, которая принимает строку и воз-
    вращает объект datetime из этой строки. Формат даты и време-
    ни можно использовать любой."""
    return datetime.strptime(stroka, '%Y-%m-%d %H:%M:%S.%f')


def var3(x: int) -> datetime.now():
    """3. Написать функцию, которая принимает целочисленное
    значение x и возвращает текущую дату, прибавив к году x."""
    year = int(str(datetime.now())[:4]) + x
    return datetime.strptime(str(year) + str(datetime.now())[4:], '%Y-%m-%d %H:%M:%S.%f')


def var4(date: datetime) -> int:
    """4. Написать функцию, которая принимает объект datetime
    и возвращает номер недели."""
    return date.isocalendar()[1]


def var5(date: datetime) -> int:
    """5. Написать функцию, которая принимает объект datetime
    и возвращает номер дня в году."""
    return date.strftime('%j')


def var6(date1: datetime, date2: datetime) -> int:
    """6. Написать функцию, которая принимает два объекта
    datetime и возвращает число по модулю дней между ними."""
    return abs((date1 - date2).days)


def var7(date: datetime, day_of_week: str) -> int:
    """7. Написать функцию, которая принимает объект datetime
    и возвращает третью среду месяца."""

    week_day_dict = {"понедельник" : 1, "вторник": 2, "среда": 3, "четверг": 4, "пятница": 5, "суббота": 6,
                     "воскресенье": 7}
    day = date.day % 7 # оставим от номера дня в месяце остаток от деления на 7
    # print("что за день такой?", day) # для отладки
    day_of_week = week_day_dict.get(day_of_week)
    # print("получим номер дня недели по словарю", day_of_week) # тоже для отладки
    # немного индийского кода полезно для здоровья(нет)
    if day_of_week == 1:
        return day + 16
    if day_of_week == 2:
        return day + 15
    if day_of_week == 3:
        return day + 14
    if day_of_week == 4:
        return day + 13
    if day_of_week == 5:
        return day + 12
    if day_of_week == 6:
        return day + 11
    if day_of_week == 7:
        return day + 10


def var8(x: int) -> list[datetime]: # not done
    """8. Написать функцию, которая принимает целое число x и
    возвращает список из 20 объектов datetime с интервалами меж-
    ду днями равными x. За первоначальное значение datetime сле-
    дует принять текущую дату."""

    date = datetime.now() # берем текущую дату
    list1 = [] # создаем пустой список
    x1 = x
    for i in range(20):
        list1.append(datetime.now() + timedelta(days=float(x1)))
        x1 += x
    return list1


def var9(date: datetime) -> datetime.timestamp:
    """9. Написать функцию, которая принимает объект datetime
    и возвращает временную метку (timestamp) из данного объекта."""
    return date.timestamp()


def var10(gmt: str) -> datetime:
    """10. Написать функцию, которая принимает строку, содер-
    жащую GMT, и возвращает смещённое значение текущей даты
    и времени."""
    # советую зарегаться на stackoverflow
    # а как добавить ко времени gmt?
    # ответ на вопросический будет по ссылке(учитесь гуглить)
    # https://ru.stackoverflow.com/questions/659229/%D0%9A%D0%B0%D0%BA-%D0%BA-%D0%BD%D1%8B%D0%BD%D0%B5%D1%88%D0%BD%D0%B5%D0%B9-%D0%B4%D0%B0%D1%82%D0%B5-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-30-%D0%BC%D0%B8%D0%BD%D1%83%D1%82
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time) # для отладки
    # print("Your Time Zone is GMT", strftime("%z", gmtime())) # для отладки
    print(datetime.now() + timedelta(minutes=float(gmt) * 60)) # преобразую строку в число и добавлю к объекту
    # datetime с помощью функции timedelta


def var11(path: str) -> list[str]:
    """11. Написать функцию, которая принимает путь к директо-
    рии и возвращает список с наименованиями файлов, которые
    хранятся в полученной директории."""
    return os.listdir(path)


def var12(path: str, file_name: str) -> str:
    """12. Написать функцию, которая принимает путь к директо-
    рии и наименование файла и возвращает полный путь к полу-
    ченному файлу."""
    if file_name in os.listdir(path):
        return path + '/' + file_name


def var13(list_of_path: list) -> int:
    """13. Написать функцию, которая принимает список путей и
    возвращает число путей, которые являются директорией."""
    counter = 0
    for element in list_of_path:
        if '.' not in ('C:/Users/lefru/Desktop/python_labs/Python_lab/' + element): # директорией считаем то, что не
            # имеет расширения в виде знака "." (точка)
            counter += 1
    return counter


def var14(path: str): # доделать
    """14. Написать функцию, которая принимает путь к директо-
    рии и удаляет в ней все файлы, а вместо них создает директо-
    рии с тем же наименованием, что и удаленные файлы без зна-
    чения расширения."""
    # сначала запомним все названия файлов в список
    # теперь удалим все файлы без расширения
    # создадим пустые папки с названиями фалов, у которых были расширения


def var15(): # доделать
    """15. Написать функцию относительно задания 8, которая
    принимает созданные 20 объектов datetime и создает для значе-
    ний года, месяца и дня вложенные директории. Например, зна-
    чение 2019-09-02 создаст три директории. Корневой будет
    2019, внутри неё 09 и т.д. Стоит отметить, что значение другого
    объекта 2019-07-02 создаст в ранее созданной директории 2019
    директорию с наименованием 07."""


def var16(): # доделать
    """16. Написать функцию, которая принимает список списков
    и создает структуру вложенных директорий и текстовых фай-
    лов относительно входящего списка, где наименованием дирек-
    тории будет являться номер вложенного списка, а наименова-
    нием файла значение элемента списка. Например, для списка
    вида [1,[1,2]] должны быть созданы три директории и три фай-
    ла, где корневая директория будет хранить файл 1.txt и дирек-
    торию под именем 1, в которой будут находиться файлы 1.txt и
    2.txt."""


if __name__ == "__main__":
    print('Вариант 1 ', var1(datetime.now()))
    print('Вариант 2 ', var2(str(datetime.now())))
    print('Вариант 3 ', var3(15))
    print('Вариант 4 ', var4(datetime.today()))
    print('Вариант 5 ', var5(datetime.today()))
    print('Вариант 6 ', var6(datetime.now(), datetime(2021, 1, 1)))
    print('Вариант 7 номер третьей среды месяца', var7(datetime.now(), "среда"))
    print('Вариант 8 список из 20 объектов datetime с интревалами в n дней', var8(2))
    print('Вариант 9 ', var9(datetime.now()))
    print('Вариант 10 ', var10('-3'))
    print('Вариант 11 ', var11('C:/Users/lefru/Desktop/python_labs/Python_lab'))
    print('Вариант 12 ', var12('C:/Users/lefru/Desktop/python_labs/Python_lab', 'README.md')) # доделать
    print('Вариант 13 ', var13(var11('C:/Users/lefru/Desktop/python_labs/Python_lab')))
    print('Вариант 14 ', var14('C:/Users/lefru/Desktop/kek')) # доделать
    print('Вариант 15 ', var15()) # доделать
    print('Вариант 16 ', var16()) # доделать
