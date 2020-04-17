try:
    with open('02.txt', 'r') as f:
        lines = f.readlines()
        print('Всего строк: ' + str(len(lines)))
        [print('В строке' + str(i+1) + ': ' + str(len(value) - 1) + ' символов') for i, value in enumerate(lines)]
except IOError:
    print("Произошла ошибка ввода-вывода!")
