import os.path
from functools import reduce, partial

try:
    if os.path.exists('05.txt') is False:
        open('05.txt', 'tw', encoding='utf-8').close()

    with open('05.txt', 'w') as f:
        [f.write(str(value) + '\n') for value in range(0, 1000)]

    with open('05.txt', 'r') as f:
        print('Всего: ' + str(reduce(lambda x, y: x + y, [int(value) for value in f.readlines()])))
except IOError:
    print("Произошла ошибка ввода-вывода!")