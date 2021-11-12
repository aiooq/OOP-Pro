'''1. Реализовать класс Matrix (матрица). 
    Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
        Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
        Примеры матриц вы найдете в методичке.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
        Результатом сложения должна быть новая матрица.
        Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class Matrix:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return "\n"+" \n".join(str(i) for i in self.values)+"\n"

    def __eq__(self, other):
        if len(self.values) != len(other.values):
            return False
        for i in range(len(self.values)):
            if len(self.values[i]) != len(other.values[i]):
                return False
        return True

    def __add__(self, other):
        if not self.__eq__(other):
            return TypeError

        return Matrix([[self.values[i][j] + other.values[i][j]  
                for j in range (len(self.values[i]))] 
            for i in range(len(self.values))])

class Task:
    def __call__(self):
        print(__doc__)
        config = (({"def":self.main}))
        return config

    def main(self, value, out):

        matrix_1 = Matrix([[31,22],[37,43],[51,86]])
        matrix_2 = Matrix([[3,5,32],[2,4,6],[-1,64,-8]])
        matrix_3 = Matrix([[3,5,8,3],[8,3,7,1]])

        print(matrix_1)
        print(matrix_2)
        print(matrix_3)
        
        print(matrix_1+matrix_1)
        print(matrix_2+matrix_2)
        print(matrix_3+matrix_3)

        # Некорректное сложение!
        print(f"Если складываем матрицы разной структуры {matrix_1+matrix_3}")

main()([Task()()])