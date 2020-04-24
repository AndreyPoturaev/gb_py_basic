# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

hours, per_hour, prize = argv[1:]
hours_int = None if not hours.isdigit() else int(hours)
per_hour_int = None if not per_hour.isdigit() else int(per_hour)
prize_int = None if not prize.isdigit() else int(prize)

if hours_int is None or per_hour_int is None or prize_int is None:
    print("Unsupported parameter type")
else:
    print(f"Salary is {hours_int*per_hour_int + prize_int}")