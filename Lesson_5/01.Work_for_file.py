import os.path

try:
    if os.path.exists('01.txt') is False:
        open('01.txt', 'tw', encoding='utf-8').close()

    with open('01.txt', 'a') as f:
        while True:
            t = input('Введите данные:')
            if t != '':
                f.writelines(t + "\n")
            else:
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")
