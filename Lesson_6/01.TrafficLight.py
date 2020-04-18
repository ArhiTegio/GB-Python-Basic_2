from enum import Enum
from itertools import cycle
from time import sleep


class Color(Enum):
    Red = 1
    Yellow = 2
    Green = 3


class TrafficLight:
    __dict_sec = {Color.Red: (7, Color.Green), Color.Yellow: (2, Color.Red), Color.Green: (3, Color.Yellow)}
    _old_color = Color.Yellow
    _color = Color.Green

    def running(self):

        for value in cycle(self.__dict_sec):
            self._old_color = self._color
            self._color = value

            if self._color in self.__dict_sec.keys() and len(self.__dict_sec[self._color]) == 2 and \
                    self._old_color == self.__dict_sec[self._color][1]:
                for i in range(0, self.__dict_sec[value][0]):
                    print(str(value.name) + ' сек ' + str(self.__dict_sec[value][0] - i))
                    sleep(1)
            else:
                print('Ошибка! Последовательность цветов не соответствует. ({} - {} != {} - {} )'.format(
                    self._old_color, self._color, self.__dict_sec[self._color][1], self._color))


trLight = TrafficLight()
trLight.running()
