companyInfo = {
    "Ename": "Akbar hossain",
    "age": 32,
    "married": False,
    "list": ["name1", "name2", "name3"],
}

# print(companyInfo["Ename"])

# print(companyInfo)

# print(type(companyInfo))

# x = companyInfo.values()

# companyInfo["age"] = 35
# print(x)


# print(companyInfo.items())

# update
# companyInfo["married"] = True
# print(companyInfo)

# companyInfo.update({"Ename": "Arnob"})
# print(companyInfo)

# Add
# companyInfo["companyName"] = "World Tour"
# print(companyInfo)

# companyInfo.update({"companyName2": "Beach View"})
# print(companyInfo)

# companyInfo.pop("list")
# print(companyInfo)

# companyInfo.popitem()
# print(companyInfo)

# del companyInfo["Ename"]
# print(companyInfo)

# companyInfo.clear()
# print(companyInfo)

# loop in dict
# for i in companyInfo:
#     print(companyInfo[i])

# for i in companyInfo.values():
#     print(i)

# for i in companyInfo.keys():
#     print(i)

# for i, j in companyInfo.items():
#     print(i, j)


# copy
# x = companyInfo.copy()
# print(x)

# y = dict(companyInfo)
# print(y)

# nested dictionary
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily = {"child1": child1, "child2": child2, "child3": child3}

# print(myfamily["child1"]["year"])

for i, j in myfamily.items():
    print(i)

    for k in j:
        print(k + ":", j[k])
