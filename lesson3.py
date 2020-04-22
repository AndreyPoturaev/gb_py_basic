# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def l1():
    def func(one, two):
        if not one.isdigit() or not two.isdigit() or int(two) == 0:
            return None
        return int(one) / int(two)
    inp_one = input("Enter first value:")
    inp_two = input("Enter second value:")
    print(func(inp_one, inp_two))

# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def l2():
    def func(name, surname, year, city, email, phone):
        return f"Person: {surname} {name} from {city}, born {year}. Contact info: {email}, {phone}"
    print(func(
        city="Moscow",
        name="Andrey",
        surname="Poturaev",
        year=1983,
        email="andrey.poturaev@yandex.ru",
        phone=89104255336
    ))

# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def l3():
    def func(*args):
        args_list = list(args)
        l = len(args_list)
        if l != 3 : raise Exception("Unsupported parameters count")
        args_list.sort()
        return args_list[l-1] + args_list[l-2]
    print(func(1,2,3))

# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def l4():
    def func(x, y):
        """**"""
        if type(x) is not int or type(y) is not int or y > 0 : raise Exception("Unsupported parameters")
        return 1 / (x ** abs(y))

    print(func(2, -5))

    def func2(x,y):
        """loop"""
        if type(x) is not int or type(y) is not int or y > 0: raise Exception("Unsupported parameters")
        res = x
        while y <= 0:
            x, y = x*x, y + 1
        return 1/x

    print(func(2, -5))

# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
from functools import reduce
def l5():
    sum = 0
    while True:
        inp = input("Enter list of numbers or '@':")
        if inp == '@': return
        inp_list = inp.split(' ')
        sum = sum + reduce(lambda i1, i2: int(i1) + int(i2), inp_list, 0)
        print(sum)

    print(sum)

# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def l6():
    def int_func(word):
        return word.capitalize()
    inp = input("Enter string:")
    inp_list = inp.split(' ')
    res = reduce(
        lambda s1,s2: f"{s1} {s2}",
        map(
            lambda s: int_func(s),
            inp_list
        )
    )
    print(res)

l1()
l2()
l3()
l4()
l5()
l6()