from functools import reduce, partial

try:
    with open('02.txt', 'r') as f:
        lines = [value.split(' ') for value in f.readlines()]
        print('Сотрудники с окладом менее 20000:')
        [print(value[0] + ' ' + str(int(value[1]))) for value in lines if int(value[1]) < 20000]
        print('Средний доход сотрудников: ' +
              str(round(reduce(lambda x, y: x + y, [int(value[1]) for value in lines])/len(lines), 2)))
except IOError:
    print("Произошла ошибка ввода-вывода!")