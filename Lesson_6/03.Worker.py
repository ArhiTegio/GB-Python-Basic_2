from enum import Enum
from functools import reduce


class Positions(Enum):
    sales_manager = 1,
    head_of_sales = 2,
    deputy_director_finance = 3,
    director = 4,


class TypeIncame(Enum):
    wage = 1,
    bonus = 2,


class Worker:
    name = 'Петров'
    surname = 'Петрович'
    position = Positions.sales_manager
    _cam = {}

    def __init__(self, name, surname, *incames):
        self.name = name
        self.surname = surname
        for e in enumerate(incames[0]):
            if e[0] < TypeIncame.__len__() and str.isdigit(e[1]):
                self._cam.update({list(TypeIncame)[e[0]]: int(e[1])})


class Position (Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return reduce(lambda x, y: x + y, [b for a, b in self._cam.items()])


pos = Position(input('Введите имя: ').capitalize(), input('Введите фамилию: ').capitalize(),
               [input('Введите ' + str(list(TypeIncame)[i]) + ': ') for i in range(0, TypeIncame.__len__())])
print(pos.get_full_name())
print(pos.get_total_income())
