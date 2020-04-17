class Road:
    __length_m = 0
    __width_m = 0

    def __init__(self, length_m, width_m):
        self.__length_m = length_m
        self.__width_m = width_m

    def get_result(self):
        answer = (self.__length_m * self.__width_m * 25 * 5) / 1000
        print(str(self.__length_m) + 'м * ' + str(self.__width_m) + 'м * 25кг/м2 * 5см = ' + str(answer) + ' т')
        return answer


road = Road(20, 5000)
road.get_result()
