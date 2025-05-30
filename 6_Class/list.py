name1 = ["Arnob", "Sami", "Karim", "Rahim", "Fahim"]
number = ["4", "7", "1", "5", "5", "7"]
# indexing
# print(names[1])

# negative indexing
# print(names[-1])

# range
# print(names[1:4])

# append
# names.append("tamim")
# print(names)

# insert
# names.insert(1, "tamim")
# print(names)

# extend
# name1.extend(name2)
# print(name1)


# remove
# name1.remove("Sami")
# print(name1)

# pop
# name1.pop(2)
# print(name1)

# del
# del name2[2]
# print(name2)

# clear
# name2.clear()
# print(name2)


# for loop
# for i in name1:
#     print(i)

# range
# for i in range(len(name1)):
#     print(name1[i])


# while loop
# i = 0
# while i < len(name1):
#     print(name1[i])
#     i = i + 1

# sort
# number.reverse()
# print(number)

# decending
# number.sort(reverse=True)
# print(number)


# copy
# new_list = name1.copy()
# print(new_list)

# list
# new_list = list(name1)
# print(new_list)

# operator
# new_list = name1[:]
# print(new_list)

# join
# print(name1 + number)

# list comprehension
# newList = []
# for i in name1:
#     if "a" in i:
#         newList.append(i)

# print(newList)

# print(number.count("4"))


# duplicate number remove from a list
number = ["4", "7", "1", "5", "5", "7"]

unique_item = []

for i in number:
    if i not in unique_item:
        unique_item.append(i)
print(unique_item)
