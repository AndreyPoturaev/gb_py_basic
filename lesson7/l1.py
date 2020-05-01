# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ""
        for x in self.data:
             result += " ".join(map(str, x)) + "\n"
        return result

    def __add__(self, other):
        new_data = []
        for i, x in enumerate(self.data):
            new_row = []
            for j, y in enumerate(x):
                new_row.append(y + other.data[i][j])
            new_data.append(new_row)
        return Matrix(new_data)

def l1():
    m1 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    m2 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    m3 = m1 + m2

    print("M1: \n" + str(m1))
    print("M2: \n" + str(m2))
    print("M3: \n" + str(m3))

l1()