# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Item):
    def __init__(self, v):
        self.__v = v

    @property
    def v(self):
        return self.__v

    @property
    def consumption(self):
        return self.__v/6.5 + 0.5

class Suit(Item):
    def __init__(self, h):
        self.__h = h

    @property
    def h(self):
        return self.__h

    @property
    def consumption(self):
        return self.__h*2 + 0.3

def l2():
    c = Coat(52)
    print(c.v)
    print(c.consumption)

    s = Suit(170)
    print(s.h)
    print(s.consumption)

l2()