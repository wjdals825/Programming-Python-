for x in range(3, 9, 2) : 
    print(x)

for ch in "Love" : 
    print(ch)

for item in ["hiphop", "dance music"] : 
    print(item + '즐겨듣는다.') 

for item in (2560,1440) : 
    print(item)
pl = {"C":1972, "JAVA":1995, "Python":1991}

for key in pl : 
    print(key, ":", pl[key])

for key, value in pl.items():
    print(key, ":", value)

for item in {"HTML5", "CSS3", "JAVASCRIPT"} : 
    print(item+"를 할 수 있다.")
#리스트 안의 리스트
table = [
    ["월","화","수"], 
    [1,2,3]
]
for row in table:
    for col in row:
        print(col)
    print("================================")
    #순서가 없다 (랜덤임)
    # , 는 공백포함 + 는 공백미포함