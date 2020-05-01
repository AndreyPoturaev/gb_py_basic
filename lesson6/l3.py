# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)

from functools import reduce

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position, self._income = name, surname, position, { "wage" : wage, "bonus" : bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

def l3():
    w1 = Position("Petr", "Petrov", "HR", 1000, 200)
    print(w1.get_full_name())
    print(w1.get_total_income())


l3()
