import random

def check (num):
    if num in hash:
        return False
    else:
        hash.add(num)
        return True


arr = [random.randint(0, 10) for x in range(0, 30)]
hash = set()
print(arr)
print([a for a in arr if check(a)])
