from enum import Enum


class Color(Enum):
    Red = 1
    Yellow = 2
    Green = 3


class Car:
    speed = 0
    color = Color.Red
    name = ""
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        pass

    def stop(self):
        pass

    def turn_direction(self):
        pass

    def show_speed(self):
        print('{} - Скорость соствляет: {}'.format(str(self)[str(self).find('.') + 1:str(self).find(' ')], self.speed))
        return self.speed




class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('{} - Превышение скорости на {}'.format(str(self)[str(self).find('.') + 1
                                                                  :str(self).find(' ')], self.speed - 60))
        super().show_speed()


class SportCar(Car):
    def show_speed(self):
        super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('{} - Превышение скорости на {}'.format(str(self)[str(self).find('.') + 1:
                                                               str(self).find(' ')], self.speed - 40))
        super().show_speed()


class PoliceCar(Car):
    def show_speed(self):
        super().show_speed()


if __name__ == "__main__":
    car_town = TownCar(80, Color.Red, 'Carmageddon_down_for_Angels_v0.5beta', False)
    car_town.show_speed()

    car_sport = SportCar(80, Color.Red, 'Carmageddon_down_for_Angels_v0.5beta', False)
    car_sport.show_speed()

    car_worker = WorkCar(80, Color.Red, 'Carmageddon_down_for_Angels_v0.5beta', False)
    car_worker.show_speed()

    car_police = PoliceCar(80, Color.Red, 'Carmageddon_down_for_Angels_v0.5beta', False)
    car_police.show_speed()
