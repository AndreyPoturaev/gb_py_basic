# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
def l2():
    first_list = [1, 2, 6, 2, 5, 3, 7, 8, 8] # [2, 6, 5, 7, 8]

    def filter_list(func, list):
        l = len(list)
        if l <= 1 : return list
        index = 1
        while index < l:
            if func(list[index-1], list[index]): yield list[index]
            index = index + 1


    second_list = [x for x in filter_list(lambda one, two: None if two <= one else two, first_list) if x != None]

    print(second_list)

# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
def l3():
    first_list = range(20, 240, 1)
    second_list = [x for x in first_list if x % 20 == 0 or x % 21 == 0]
    print(second_list)


# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
def l4():
    first_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 2, 3, 9, 10] #[1, 4, 5, 6, 7, 9, 10]
    second_list = [x for x in first_list if first_list.count(x) == 1]
    print(second_list)

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

def l5():
    first_list = range(100, 1000, 2)
    result = reduce(lambda one, two: one*two, first_list, 1)
    print(result)
    print(type(result))

# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
from itertools import count, cycle

def l6():
    def iterator_a(start):
        return count(start)

    iter = iterator_a(45)
    print(next(iter))

    def iterator_b(list):
        return cycle(list)

    iter2 = iterator_b([1,2,3])
    print(next(iter2))
    print(next(iter2))
    print(next(iter2))
    print(next(iter2))

# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
def l7():
    def fibo_gen():
        yield 1
        for x in count(2):
            yield reduce(lambda one,two: one*two, range(1,x), 1)

    index = 0
    for x in fibo_gen():
        if index >= 15:
            break
        print(f'{x} ')
        index = index + 1

l2()
l3()
l4()
l5()
l6()
l7()
