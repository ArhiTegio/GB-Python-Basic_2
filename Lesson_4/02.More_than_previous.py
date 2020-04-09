from functools import reduce, partial
import random


arr = [random.randint(0, 100) for x in range(0, 20)]
arr3 = arr * 3
print(arr)
print([a for a, b in zip(arr, arr3[len(arr) + 1:]) if a > b])
