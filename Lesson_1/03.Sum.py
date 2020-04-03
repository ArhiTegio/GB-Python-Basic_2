print('Найдем сумму чисел n + nn + nnn')
print('Введите число n: ')
n = ''
while True:
    n = input()
    n.isdigit()
    if n.isdigit():
        break
    else:
        print('Введите число n: ')

print(n + " + " + n + n + " + " + n + n + n + " = " + str(int(n) + int(n + n) + int(n + n + n)))
