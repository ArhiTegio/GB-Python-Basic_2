print('Hello world')
x = 111
y = 3
print(x * y)

print('Математические вычисления.')
print('Введите первое число: ')

num1 = ''
while True:
    num1 = input()
    num1.isdigit()
    if num1.isdigit():
        break
    else:
        print('Введите первое число: ')

print('Введите второе число: ')
num2 = ''
while True:
    num2 = input()
    num2.isdigit()
    if num2.isdigit():
        break
    else:
        print('Введите второе число: ')

print(str(num1) + " * " + str(num2) + " = " + str(int(num1) * int(num2)))

txt = input('Введите любую строку: ')
print('Вы ввели: ' + txt)
