def findEvenOdd(numbersList):
    even = []
    odd = []

    for i in numbersList:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    even.sort()
    odd.sort(reverse=True)

    return (even, odd)


n = input("Enter numbers here: ")

list_n = list(map(int, n.split()))

result = findEvenOdd(list_n)

print("Even Numbers (Ascending): ", result[0])
print("Odd Numbers (Descending): ", result[1])
print("Result Tuple: ", result)
