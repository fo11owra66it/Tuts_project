# task 01
# Создать файл simple.py, и сделайте в нем следующую задачу:
# a = 2
# b = ???
# print(a + b)
# задать значение переменной b, чтобы результат был 2.5
a = 2
b = 0.5
print(a + b)

# task 02
# name = 'ВСТАВЬТЕ ВАШЕ ИМЯ'
# print(???)
# Cделать так, чтобы программа 
# приветствовала вас, используя переменную name 
# и форматирование строк например "Привет, Миша!"
name = 'Simon'
print(f'Hello {name}!')

# task 03
# v = input('Введите число от 1 до 10: ')
# print(???) 
# поправить код, чтобы выводилось число
# на 10 больше, чем введённое
# например, пользователь ввел 10 
# программа вывела 20
v = input('Введите число от 1 до 10: ')
print(int(v) + 10)

# task 04
# name = input('Введите ваше имя: ')
# print(???)
# # поправьте код, чтобы выводилась строка
# Привет, ИМЯ! Как дела?
name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

# task 05
# Вывести на экран при помощи print() результат работы:
print(float('1'))    # => 1.0
print(int('2.5'))    # => Error
print(bool(1))    # => True
print(bool(''))    # => False
print(bool(0))    # => False