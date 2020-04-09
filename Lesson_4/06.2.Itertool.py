from itertools import cycle
from time import sleep
import random

for i in cycle([random.randint(0, 100) for a in range(0, 6)]):
    print(i)
    sleep(0.5)
