# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, color, name, is_police):
        self.color, self.name, self.is_police = color, name, is_police

    def go(self, speed = 60):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        pass

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        print("Превышение" if self.speed > 60 else "Скорость в норме")

class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        print("Превышение" if self.speed > 40 else "Скорость в норме")

class PoliceCar():
    def __init__(self, color, name):
        super().__init__(color, name, True)


def l4():
    tc = TownCar("red", "Ford")
    wc = WorkCar("white", "GAZ")

    tc.go(55)
    wc.go(45)

    tc.show_speed()
    wc.show_speed()

    tc.stop()
    tc.show_speed()


l4()
