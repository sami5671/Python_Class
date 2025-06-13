from collections import OrderedDict

n = int(input())
items = OrderedDict()

for i in range(n):
    part = input().split()
    price = int(part[-1])
    item_name = " ".join(part[:-1])

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for i, j in items.items():
    print(i, j)
