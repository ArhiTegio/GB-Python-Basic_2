print('Расчет продолжительности тренировок для спортсмена из начальных и конечных параиетров')
print('Введите начальные значение: ')
a = ''
while True:
    a = input()
    a.isdigit()
    if a.isdigit():
        break
    else:
        print('Введите начальные значение: ')

print('Введите расчетное значение: ')
b = ''
while True:
    b = input()
    b.isdigit()
    if b.isdigit():
        break
    else:
        print('Введите расчетное значение: ')

day = 0
result = int(a)
found_result = int(b)
while True:
    day += 1
    if result >= found_result:
        break
    print(str(day) + '-й день: ' + str(round(result, 2)))
    result *= 1.1
print(str(day) + '-й день: ' + str(round(result, 2)))
print('------------------------------------------------')
print('На ' + str(day) + '-й день спортсмен достиг результата')
