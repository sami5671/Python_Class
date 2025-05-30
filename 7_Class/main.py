item = ("Laptop", "Ram", "Rom", "Cable", "Ram")

# print(item[1:3])
# print(type(item))

# if "Rom" in item:
#     print("YES")

x = list(item)

# y = list(x)
# y[1] = "PC"

# x = tuple(y)
# print(x)


# y = list(x)
# y.append("Arnob")
# item = tuple(y)
# print(y)

# y = ("sami",)
# item = item + y
# print(item)

# unpacking
# (a, b, *c) = item
# print(a)

# loop
# for i in item:
#     print(i)

# while
# i = 0
# while i < len(item):
#     print(item[i])
#     i = i + 1


# item2 = (1, 2, 4)

# t3 = item + item2
# print(t3)

# i = item.index("Ram")
# print(i)


# set
names = {"arnob", "karim", "sami"}
number = {1, 2, 4}
# names = set(("arnob", "karim", "sami"))

# print(names)

# if "karibjm" in names:
#     print("YES")
# else:
#     print("NO")

# for i in names:
#     print(i)

# names.add("rahim")
# print(names)

# update
# names.update(number)
# print(names)

# names.remove("sami")
# names.pop()

# print(names)

# union
set1 = {"arnob", "karim", "sami"}
set2 = {"a", "k", "sami"}

# set3 = set1.union(set2)
# set3 = set1 | set2
# set3 = set1.intersection(set2)
# set3 = set1 & set2

# set3 = set1.difference(set2)
# set3 = set1 - set2

# set3 = set1.symmetric_difference(set2)

# set3 = set1 ^ set2

# print(set3)

# 1. Write a Python program to sort a tuple by its float element.
# Ex: price = [('item1', '18.20'), ('item2', '15.10'), ('item3', '24.5')]

# price = [("item1", "18.20"), ("item2", "15.10"), ("item3", "24.5")]

# final_price_sorted = sorted(price, key=lambda x: float(x[1]), reverse=False)
# print(final_price_sorted)


# 2. Write a Python program to count the elements in a list until an element is a tuple.
# Ex: num = [10, 20, 30, (10, 20), 40]
# Result: 3


def checkTuple(i):
    if type(i) == tuple:
        return True
    else:
        return False


num = [10, 20, 30, (10, 20), 40]
count = 0

for i in num:
    if checkTuple(i):
        break
    count = count + 1

print(count)
