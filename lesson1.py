#Поработайте с переменными,
#создайте несколько, выведите на экран,
#запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
def l1():
    age = 18
    name = "piter"
    print(age, name)

    age = input("Enter age:")
    name = input("Enter name:")
    print(age, name)

#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.
def convert_to_digit(str, msg="\nThis isn't a digit\n"):
    if not str.isdigit():
        print(msg)
        return None
    else:
        return int(str)


def l2():
    sec = input("Enter time in seconds:")

    total_sec = convert_to_digit(sec)
    if total_sec is None:
        return
    hour = total_sec // 3600
    min = total_sec % 3600 // 60
    sec = total_sec % 3600 % 60
    print(f"{hour:0>2}:{min:0>2}:{sec:0>2}")


#Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
def l3():
    val = input("Enter digit:")
    val_int = convert_to_digit(val)
    if val_int is None:
        return
    val2_int = convert_to_digit(val + val)
    val3_int = convert_to_digit(val + val + val)
    print(f"{val_int}+{val2_int}+{val3_int}={val_int+val2_int+val3_int}")

#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции
def l4():
    val = input("Enter number:")
    val_int = convert_to_digit(val)
    if val_int is None:
        return
    max_digit = 0
    index = 0
    while True:
        if index >= len(val):
            break
        next_digit = int(val[index])
        if next_digit > max_digit:
            max_digit = next_digit
        index = index + 1
    print("Max digit is ", max_digit)

#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
def l5():
    rev = input("Enter revenue, $:")
    rev_int = convert_to_digit(rev)
    cost = input("Enter costs, $:")
    cost_int = convert_to_digit(cost)
    if rev_int is None or cost_int is None:
        return
    ok = rev_int > cost_int
    print("\nПрибыль" if ok else "\nУбыток")
    if ok:
        print(f"\nРентабельность: {(rev_int - cost_int)*100 / rev_int}%")
        empl = input("\nEnter employees count:")
        empl_int = convert_to_digit(empl)
        print(f"Рентабельность в расчете на сотрудника: { (rev_int - cost_int)/ empl_int} $")

#Спортсмен занимается ежедневными пробежками.
#В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
def l6():
    a = input("Enter a:")
    a_int = convert_to_digit(a)
    b = input("Enter b:")
    b_int = convert_to_digit(b)
    if a_int is None or b_int is None:
        return
    prev = float(a_int)
    iteration = 1
    while prev < b_int:
        prev = prev * 1.1
        iteration = iteration + 1
    print("Day: ", iteration)

l1()
l2()
l3()
l4()
l5()
l6()



