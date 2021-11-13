'''3. Реализовать программу работы с органическими клетками. 
    Необходимо создать класс Клетка. 
    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
    В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. 
    В методе деления должно осуществляться округление значения до целого числа.
    Сложение. 
        Объединение двух клеток. 
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    Вычитание. 
        Участвуют две клетки. 
        Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
    Умножение. 
        Создается общая клетка из двух. 
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
    Деление. 
        Создается общая клетка из двух. 
        Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
        Данный метод позволяет организовать ячейки по рядам.
        Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
        Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
        Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
        Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
            Подсказка: подробный список операторов для перегрузки доступен по ссылке.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Cell:
    def __init__(self, count):
        if count<=0:
            raise OwnError("Количество клеток меньше или равно нулю")
        self.count = count
        print(f"({self.count}): {self.__call__()}")

    def __call__(self):
        return "".join(["*" for i in range(self.count)])

    def __eq__(self, other):
        return type(self) == type(other)      

    def __add__(self, other):
        if not self.__eq__(other):
            raise TypeError
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if not self.__eq__(other):
            raise TypeError
        value = self.count - other.count
        # Необязательно, так как проверка происходит при создании нового экземляра
        # if value<=0:
        #     raise OwnError("Разность двух клеток меньше или равна нулю")
        return Cell(value)

    def __mul__(self, other):
        if not self.__eq__(other):
            raise TypeError
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        if not self.__eq__(other):
            raise TypeError
        return Cell(round(self.count / other.count))

    @staticmethod
    def make_order(other, cells_in_row):
        if not isinstance(other, Cell):
            raise TypeError
        return "\n".join(["".join(["*" for i in range(cells_in_row)]) for i in range(other.count//cells_in_row)])+"\n"+"".join(["*" for i in range(other.count%cells_in_row)])

class Task:
    def __call__(self):
        print(__doc__)
        print("".join(["=" for i in range(100)]))
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        cell_7=Cell(7)
        cell_20=Cell(20)

        # Арифметических операции
        cell_27=cell_7+cell_20
        cell_13=cell_20-cell_7
        cell_140=cell_20*cell_7
        cell_3=cell_20/cell_7

        # Ошибочные варианты арифметических операций
        try:
            cell_raise=cell_7-cell_20
        except Exception as e:
            print(e)  
        
        try:
            cell_raise=cell_7/cell_20
        except Exception as e:
            print(e)         

        # Вызываем статический метод, который возвращает специальную строку по заданным аргументам и печатаем
        print(Cell.make_order(cell_13,5))


main()([Task()()])