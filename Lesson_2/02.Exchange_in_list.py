print('Обмен данными между значениями в листе')
print('Заполним лист данными (для завершения введите пустую строку): /n')
l_any_elements = []
while True:
    e = input('Введите любое значение: ')
    if e != '':
        l_any_elements.append(e)
    else:
        break

print('list[' + ''.join([str(l_any_elements[num] + ', ') for num in range(len(l_any_elements))]) + ']')

if len(l_any_elements) > 0:
    avg = int(len(l_any_elements) / 2)
    for e in range(0, avg, 2):
        l_any_elements[e], l_any_elements[len(l_any_elements) - e - 1] = \
            l_any_elements[len(l_any_elements) - e - 1], l_any_elements[e]

print('list[' + ''.join([str(l_any_elements[num] + ', ') for num in range(len(l_any_elements))]) + ']')
