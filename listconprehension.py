array1 = []
for i in range(1, 10+1, 2):
    array1.append(i**2) #거듭제곱 
print("array1 :", array1)

array2 = [i**2 for i in range(1, 10+1, 2)]
print("array2 :", array2)

array3 = [i**2 for i in range(1, 10+1, 2) if i**2 > 30]
print("array3 :", array3)

array4 = []
for i in range(1, 10+1, 2):
    if i**2 > 30:
        array4.append(i**2)
print("array4 :", array4)