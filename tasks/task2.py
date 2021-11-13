'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
    К типам одежды в этом проекте относятся пальто и костюм. 
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
    Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
    Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. 
    Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

from abc import abstractmethod

class Clothes:
    def __init__(self, name):
        self.name = name
        self.__call__()

    def __call__(self):
        print(self.__str__())

    @abstractmethod
    def __str__(self):
        return self.name        

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.__init__(self, "Пальто")

    def __str__(self):
        return f"{self.name}, размер: {self.size}, расход ткани: {self.consumption}" 

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Clothes.__init__(self, "Костюм")

    def __str__(self):
        return f"{self.name}, рост: {self.height}, расход ткани: {self.consumption}"

    @property
    def consumption(self):
        return 2 * self.height + 0.3     

class Task:
    def __call__(self):
        print(__doc__)
        print("".join(["=" for i in range(100)]))
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        сlothes = Clothes("Какая-то одежда")
        coat = Coat(50)         # Создаем объект пальто с размером в 50
        costume = Costume(50)   # Создаем объект Костюм с размером в 50

        print("\nКоллекция одежды для нового сезона:")
        clothes = [Coat(40),Costume(50),Coat(30),Costume(10),Coat(70),Costume(45)]
        print(f"\nОбщий подсчет ткани на коллекцию {sum([item.consumption for item in clothes])}")


main()([Task()()])