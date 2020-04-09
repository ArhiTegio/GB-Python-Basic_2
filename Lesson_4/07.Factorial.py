from time import sleep


def factorial():
    n = 1
    step = 1
    while(True):
        n *= step
        step += 1
        yield n


step = 0
for el in factorial():
    print('Factorial {} - {}'.format(step + 1, el))
    sleep(0.5)
    step += 1
    if step >= 15:
        break