def var1():
    """1. Написать функцию, которая принимает Json строку и
    конвертирует её в словарь."""


def var2():
    """2. Написать функцию, которая принимает путь к файлу и
    количество строк, которые требуется прочитать и возвращает
    считанные строки в файле. """


def var3():
    """3. Написать программу, которая принимает путь к файлу
    и возвращает наиболее длинное слово из него."""


def var4():
    """4. Написать функцию, которая принимает путь к файлу,
    текст и номер строки и записывает в файл полученный текст в
    указанный номер строки."""


def var5():
    """5. Написать программу, которая принимает путь к файлу
    и возвращает True или False в зависимости от того, доступен ли
    файл для чтения и записи или нет."""


def var6():
    """6. Написать функцию, которая принимает путь к HTML
    файлу и html тег («p», «h1», «article» и др.) и возвращает
    количество повторений полученного тега в файле с учетом того, что
    требуется вернуть только количество тегов, который имеет
    открывающую и закрывающую часть."""


def var7():
    """7. Написать функцию, которая принимает путь к директории,
    путь к файлу и записывает в файл информацию обо всех
    файлах в директории (формат файла, размер, дата создания).
    Информация о файлах должна быть пронумерована, а каждый
    параметр должен быть помечен. Например, «1. Test;
    Расширение файла: py; Дата создания: 2019-12-12…» и т.д."""


def ver8():
    """8. Написать функцию, которая принимает путь к двум
    файлам и возвращает количество одинаковых предложений в
    файлах. """


def ver9():
    """9. Написать функцию, которая принимает путь к файлу и
    параметр x, который может являться строкой или списком, и
    возвращает частоту повторений параметра x в строке. В случае,
    когда параметром x является список, следует вернуть словарь, в
    котором в качестве ключей будут искомые строки,
    а их значениями частота повторений."""


def ver10():
    """10.Написать функцию, которая принимает путь к HTML и
    путь к CSS файлам и возвращает словарь, в котором ключами
    выступают теги, идентификаторы или классы в файле CSS, а
    значениями список списков, где первым элементом внутреннего
    списка будет наименование тега, которые попадают под стили,
    указанные в файле CSS, а вторым – номер строк, в которых
    они находятся. Например, {'#inline-text': [[‘h1’, 29], [‘p’, 50]]}. """


def ver11():
    """11.Написать функцию, которая принимает путь к файлу и
    возвращает словарь, в котором в качестве значений выступают
    строки, а их ключами – количество символов русского алфавита.
    Символы русского следует генерировать в процессе выполнения
    функции, используя build-in функции ord() и chr()."""


def ver12():
    """12.Написать функцию, принимающую словарь, который
    может содержать любые элементы и конвертирует в Json
    только те элементы, значения которых являются списками,
    содержащими только целочисленные значения. """


def ver13():
    """13.Написать функцию, которая принимает ссылку на страницу
    с расписанием студентов ЮРГПУ(НПИ) и возвращает
    путь к файлу Json, в котором все возможные данные о
    расписании по полученной ссылке, в том числе курсе и коде учебной
    группы. Можно использовать специализированный синтаксический
    анализатор для HTML (BeatifulSoup, lxml и другие)."""
