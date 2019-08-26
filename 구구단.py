for dan in range(2, 9+1):
    for i in range(1, 9+1):
        if i > 7:
            break
        if i%2==0:
            continue
        print(dan, "x", i, "=", dan*i)
    print("==========================")