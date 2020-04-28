# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка
def l1():
    with open("l1.txt", "w") as f:
        while True:
            inp = input()
            if inp == "":
                break
            f.write(inp + '\n')


# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
from functools import reduce
def l2():
    with open("l2.txt", encoding='utf-8') as f:
        content = f.readlines()
        print(f"Lines: {len(content)}")
        print(f"Words: {sum(map(lambda x: len(x.split(' ')), content))}")


# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников
def l3():
    with open("l3.txt", encoding='utf-8') as f:
        content = f.readlines()
        empl = dict(map(lambda x: (x.split('\t')), content))
        for k in empl:
            empl[k] = int(empl[k].replace('\n', ''))

        less_then_20k = [k for k, v in empl.items() if v < 20]
        print(f"Less then 20: {less_then_20k}")
        avg_salary = sum(empl.values()) / len(empl.values())
        print(f"Avg salary: {avg_salary}")


# Создать (не программно) текстовый файл со следующим содержимым:
# One - 1
# Two - 2
# Three - 3
# Four - 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на ~русские~ цифры.
# Новый блок строк должен записываться в новый текстовый файл
def l4():
    numbers = dict()
    with open("l4_map.txt", encoding='utf-8') as f:
        content = f.readlines()
        numbers = dict(map(lambda x: (x.split(' - ')), content))
        for k in numbers:
            numbers[k] = numbers[k].replace('\n', '')
    with open("l4_input.txt", encoding='utf-8') as f_inp, open("l4_output.txt", "w") as f_out:
        for l in f_inp:
            for k, v in numbers.items():
                l = l.replace(k, v)
            f_out.write(l)
    print("done")


# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
def l5():
    with open("l5.txt", "w") as f:
        l = range(1, 1000, 3)
        f.write(' '.join(map(lambda x: str(x), l)))
    with open("l5.txt") as f:
        print(f"Sum is: {sum(map(lambda x: int(x), f.read().split(' ')))}")


# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re
def l6():
    lessons = dict()
    with open("l6.txt", encoding='utf-8') as f:
        content = f.readlines()
        lessons = dict(map(lambda x: (x.split(':')), content))
        for k in lessons:
            lessons[k] = [int(x) for x in re.sub(r'\(\S*\)\n*', '', lessons[k]).split(' ') if x != '']
    for k in lessons:
        print(f"Lesson {k}, total hours {sum(lessons[k])}")



# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста
def parse_firm(s):
    props = s.replace('\n', '').split(' ')
    p = [props[1]]
    p.extend(map(lambda x: int(x), props[2:]))
    return props[0], p

def l7():
    firms = dict()
    with open("l7.txt", encoding='utf-8') as f:
        content = f.readlines()
        firms = dict(map(parse_firm, content))

    avg_rev = {"average_profit": sum(map(lambda x: x[1] - x[2] if x[1]-x[2] > 0 else 0, firms.values())) / len(firms.values())}
    firms_rev = dict(map(lambda x: (x, abs(firms[x][1] - firms[x][2])), firms))
    result = [firms_rev, avg_rev]
    print(result)

l1()
l2()
l3()
l4()
l5()
l6()
l7()