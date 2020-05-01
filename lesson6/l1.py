# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import asyncio

class TrafficLight():
    def __init__(self):
        self.__color = "red"

    async def __to_color(self, color, wait):
        self.__color = color
        print(f"to {self.__color}")
        await asyncio.sleep(wait)

    async def running(self):
        while True:
            await self.__to_color("red", 7)
            await self.__to_color("yellow", 2)
            await self.__to_color("green", 10)

    def get_color(self):
        return self.__color

async def monitor(tl):
    while True:
        print(tl.get_color())
        await asyncio.sleep(1)

async def l1():
    tl = TrafficLight()
    await asyncio.gather(
        tl.running(),
        monitor(tl)
    )

asyncio.run(l1())
