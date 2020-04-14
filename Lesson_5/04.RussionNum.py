from Lesson_5.conv import num2text

print(num2text(1))
try:
    with open('04.txt') as f:
        wr = open('041.txt', 'w', encoding="utf-8")
        [wr.write(num2text(int(v.split(' ')[2])) + ' - ' + v.split(' ')[2]) for v in f.readlines()]
        wr.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
