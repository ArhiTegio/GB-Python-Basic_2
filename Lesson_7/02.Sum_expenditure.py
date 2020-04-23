from abc import ABC, abstractmethod


class Clothes(ABC):
    name = ''

    def __init__(self, H, V):
        self.H = H
        self.V = V

    @abstractmethod
    def fabric_consumption(self):
        return 0

    def __add__(self, other):
        if isinstance(other, Clothes):
            return self.fabric_consumption() + other.fabric_consumption()
        else:
            return self.fabric_consumption() + other

    def __int__(self):
        return int(round(self.fabric_consumption()))

    def __float__(self):
        return float(self.fabric_consumption())

    def hello(self): #Цепные вызовы методов
        print('Hello world!', end=' ')
        return self

    @property
    def testprop(self):
        return self._testprop

    @testprop.setter
    def testprop(self, value):
        self._testprop = value

    def test(self):
        pass


class Coat(Clothes):
    name = 'Пальто'

    def fabric_consumption(self):
        return self.V / 6.5 + 0.5


class Costume(Clothes):
    name = 'Костюм'

    def fabric_consumption(self):
        return 2 * self.H + 0.3


coat = Coat(2, 2)
costume1 = Costume(2, 3)
costume2 = Costume(3, 3)

print(coat + 1 + 2 + (costume1 + costume2) + 0.5)

coat.hello().hello().hello().hello()
print()
coat.testprop = 1
print(str(coat.testprop))
