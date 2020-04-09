from itertools import count
from time import sleep

for i in count(int(input('Введите число: '))):
    print(i)
    sleep(0.5)
