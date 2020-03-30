import datetime

print('Определим время')
print('Введите количество секунд: ')
sec = ''
while True:
    sec = input()
    sec.isdigit()
    if sec.isdigit():
        break
    else:
        print('Введите количество секунд: ')

print('%d:%02d:%02d' % ((int(sec) // 3600) % 24, (int(sec) // 60) % 60, int(sec) % 60))
