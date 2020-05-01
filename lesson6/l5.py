#  Реализовать класс Stationery (канцелярская принадлежность).
#  Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.”
#  Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение.
#  Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Pen: Запуск отрисовки.")

class Pencil(Stationery):
    def draw(self):
        print("Pencil: Запуск отрисовки.")

class Handle(Stationery):
    def draw(self):
        print("Handle: Запуск отрисовки.")

import sys

def handle_print_output():
    f = open("test.txt", "w")
    sys.stdout = f
    return f

def get_print_output():
    with open("test.txt", "r") as f:
        return f.readlines()

def l5():
    p = Pen("T1")
    pn = Pencil("T2")
    h = Handle("H1")

    assert p.title == "T1"
    assert pn.title == "T2"
    assert h.title == "H1"

    with handle_print_output():
        p.draw()
    assert  get_print_output() == ["Pen: Запуск отрисовки.\n"]

    with handle_print_output():
        pn.draw()
    assert get_print_output() == ["Pencil: Запуск отрисовки.\n"]

    with handle_print_output():
        h.draw()
    assert get_print_output() == ["Handle: Запуск отрисовки.\n"]

l5()
