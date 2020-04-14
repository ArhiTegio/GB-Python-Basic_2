from functools import reduce, partial
dict = {}
try:
    with open('06.txt', 'r', encoding='utf-8') as f:
        dict = {value.split(' ')[0][0:-1]: reduce(lambda x, y: x + y,
                                                  [int(v.split('(')[0]) for v in value.split(' ')
                                                   if v.split('(')[0].isdigit()]) for value in f.readlines()}
except IOError:
    print("Произошла ошибка ввода-вывода!")

print(dict)
