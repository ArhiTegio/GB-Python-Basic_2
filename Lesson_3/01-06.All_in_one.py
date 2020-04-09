import inspect


dict = {
    "Задание 1 - Деление": lambda x, y: print(0) if y == '0' else print(float(x) / float(y)),
    "Задание 2 - Личные данные": lambda name, surname, year_of_birth, city, email, telephone: print("Имя:" + name +
                                                                                                    " Фамилия:" + surname + " Год рождения:" + year_of_birth +
                                                                                                    " Город проживания:" + city + " Емайл:" + email + " Телефон:" + telephone),
    "Задание 3 - Наибольшие два аргумента": lambda x, y, z: print((float(x) + float(y) + float(z)) -
                                                                  min([float(x), float(y), float(z)])),
    "Задание 4.1 - Возведение в степень": lambda x, in_pow: print(float(x) ** float(in_pow)),
    "Задание 4.2 - Возведение в степень": lambda x, y: print(my_pow(float(x), float(y))),
    "Задание 5 - Подсчет последовательности": lambda: print(numbers()),
    "Задание 6.1 - Capitalize": lambda x: print(str(x).capitalize()),
    "Задание 6.2 - Title": lambda x: print(str(x).title())
}

for key, value in dict.items():
    print(key)
    if len(inspect.signature(value).parameters.keys()) == 0:
        value()
    if len(inspect.signature(value).parameters.keys()) == 1:
        value(input('Введите значение ' + list(inspect.signature(value).parameters.keys())[0] + ': '))
    if len(inspect.signature(value).parameters.keys()) == 2:
        value(input('Введите значение ' + list(inspect.signature(value).parameters.keys())[0] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[1] + ': '))
    if len(inspect.signature(value).parameters.keys()) == 3:
        value(input('Введите значение ' + list(inspect.signature(value).parameters.keys())[0] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[1] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[2] + ': '))
    if len(inspect.signature(value).parameters.keys()) == 6:
        value(input('Введите значение ' + list(inspect.signature(value).parameters.keys())[0] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[1] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[2] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[3] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[4] + ': '),
              input('Введите значение ' + list(inspect.signature(value).parameters.keys())[5] + ': '))


def my_pow(b, n):  # Задание 4.2 - Возведение в степень
    ab = True if n >= 0 else False
    n = abs(n)

    def even(n):  # проверка четности
        if n % 2 == 0:
            return 1
        return 0
    a = 1
    if n == 1:
        return b;
    if n == 0 & b == 0:
        return 1;
    if n == 0:
        return 0
    if not even(n):
        a = b
        n -= 1
    while n != 1:
        b *= b
        n /= 2
    b *= a

    return b if ab else 1 / b


def counting(self):
    '''Подсчет значений'''
    answer = 0
    for e in self:
        if e.isdigit():
            answer += int(e)
    return answer


def numbers():  # Задание 5 - Подсчет чисел
    answer = 0
    while True:
        nums = input('Введите последовательность число разделенным пробелом (нажмите символ ! для выхода): ')
        if nums.find('!', 0, len(nums)) == -1:
            answer += counting(nums.split(' '))
            print(answer)
        else:
            pos = nums.find('!', 0, len(nums))
            nums = nums[0:pos]
            answer += counting(nums.split(' '))
            print(answer)
            break
