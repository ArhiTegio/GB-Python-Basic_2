print('Расчет финансов фирмы')
print('Введите выручку фирмы: ')
debit = ''
while True:
    debit = input()
    debit.isdigit()
    if debit.isdigit():
        break
    else:
        print('Введите выручку фирмы: ')

print('Введите издержки фирмы: ')
credit = ''
while True:
    credit = input()
    credit.isdigit()
    if credit.isdigit():
        break
    else:
        print('Введите издержки фирмы: ')

rent = int(debit) - int(credit)
if rent > 0:
    print('Ваша рентабельность систавляет: ' + str(rent))
else:
    print('Ваши издержки составляют: ' + str(rent))

print('Введите количество сотрудников в вашей фирме: ')
crew = ''
while True:
    crew = input()
    crew.isdigit()
    if crew.isdigit():
        break
    else:
        print('Введите количество сотрудников в вашей фирме: ')

print('Прибыль фирмы в расчете на одного сотрудника составит: ' + str(rent / int(crew)))
