print('Найдем самую большую цифру в числе')
print('Введите число: ')
n = ''
while True:
    n = input()
    n.isdigit()
    if n.isdigit():
        break
    else:
        print('Введите число: ')
t = -1
for number in n:
    if int(number) > t:
        t = int(number)

print('Максимальное число будет: ' + str(t))


