from functools import reduce
import json

list = [{},{},{}]
with open('07.txt', 'r', encoding='utf-8') as f:
    temp = {v.split(' ')[0]: (int(v.split(' ')[2]) - int(v.split(' ')[3])) for v in f.readlines()}
    list[0].update({k: v for k, v in temp.items() if v >= 0})
    list[1].update({"average_profit": reduce(lambda x, y: x + y,
                                [v for k, v in temp.items() if v >= 0]) / len([v for k, v in temp.items() if v >= 0])})
    list[2].update({k: v for k, v in temp.items() if v < 0})

print(list)


with open("071.txt", "w", encoding="utf-8") as file:
    json.dump(list, file)