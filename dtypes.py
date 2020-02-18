# a = 2
# b = 3
# c = a + b
# print(c)
# c = a - b
# print(c)
# c = a * b
# print(c)
# c = a ** b
# print(c)
# c = a / b
# print(c)   # всегда вещественное число

# a = 2.5
# b = 3.1
# c = a + b
# print(c)

# a = 2.5
# b = 0.5
# c = a - b
# print(c)

# a = 2.5
# b = 1
# c = a - b
# print(c)

# a = 3
# b = 0
# c = a > b
# print(c)
# c = a < b
# print(c)
# c = a == b
# print(c)
# c = a != b
# print(c)

# a = 'Привет'
# b = "Привет"
# print(a == b)

# a = 'Привет'
# b = 'мир'
# print(a + b)

# a = 'Привет'
# b = 'мир'
# c = a + ' ' + b + '!'
# print(c)

# a = 'Привет'
# b = 'мир'
# c = '{} {}!'.format(a, b)
# print(c)

# a = 'Привет'
# b = 'мир'
# d = 2
# # c = a + ' ' + b + d + '!'  # будет ошибка, т.к разные типы данных
# # print(c)
# c = '{} {}{}!'.format(a, b, d)  # метод .format() автоматически приводит аргументы к строке
# print(c)

# user = 'Python'
# c = 'Привет {name}!'.format(name=user)
# print(c)

# user = 'Python'
# c = f'Привет {user}!'
# print(c)

# a = 'Привет'
# b = 'мир'
# c = f'{a} {b}!'   # d = len(c)
# print(len(c))     # print(d)

# a = 'Привет'.upper()
# b = 'Привет'.lower()
# c = 'привет'.capitalize()
# d = 'привет мир'.title()
# print(a, b , c, d)

# a = ' Привет '
# print(len(a))
# print(len(a.strip()))  #убираем пробелы из начала и конца строки

# a = 'Прив3т т3б3'.replace('3', 'e')    # c = a.replace('3', 'e')
# print(a)                               # print(c)
# b = 'ПриветЫ'.replace('ы', '')         # пустые кавычки – пустая строка
# print(b)

# a = 'ПриветЫ'.lower().replace('ы', '').capitalize()
# print(a)

# a = 'Привет, мир!'.replace('мир', 'python')
# print(a)

# a = 'learn.python.ru'  #разбиение строки на список по какому-либо символу
# print(a.split('.'))

# a = 'Несколько слов здесь есть, а вы что думали'
# b = a.split()   #пустые скобочки – разбивание по пробелу
# print(b)
# print(len(b))

# a = None
# b = 0
# print(a is None)
# print(b is None)   # print(b is not None)

# a = 2
# b = '2.0'
# c = 2.0
# d = True
# e = None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(e))

# name = input('Введите ваше имя: ')
# # print(name)
# print(f'Привет {name}!')

# years = int(input('Сколько вам лет?'))  # из input только str. Для смены типа обозначаем тип перед input
# years = 2020 - years
# print(f'Вы родились в {years} году!')

# print(bool('Привет'))    # если не пустая строка/число/что-то, то True. Если пустое или None, то True
# print(bool(''))
# print(bool(1))
# print(bool(0))
# print(bool(0.1))
# print(bool(-2))
# print(bool(None))

# v = int(input('Введите число от 1 до 10: '))
# print(v + 10)

# name = input('Введите ваше имя: ')
# print(f'Привет, {name}! Как дела?')