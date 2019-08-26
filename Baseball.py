# 야구게임
# 세자리 중복없는 임의의수 만들자
# 무한반복  while
#  사용자 입력을 받자 input()
# strike, ball 판정하자
# 사용자 입력한 것, strike, ball 출력하자 print()
# 임의의수랑 사용자 입력한게 같으면 HIT, break 

import random

# r0 = random.randrange(1, 9+1)
# r0 = str(r0)
# r1 = random.randrange(1, 9+1)
# r1 = str(r1)
# r2 = random.randrange(1, 9+1)
# r3 = str(r2)
# computer = r0+r1+r2
# computer = str(random.randrange(100,999+1))

# l = list(range(1,9+1)) #[1,2,3,4,5,6,7,8,9]
# random.shuffle(1) #[3,6,4,1,2,5,7,9,8]
# l[:3] #[3,6,4]
# a = ""
# for i in l[:3]:
#     a+=str(i)

# ''.join(str(i) for i in l[:3])    

l = random.sample(range(1,9+1),3)
computer = ''.join(str(i) for i in l)

#computer = "851"
while True:
    player = input("숫자 세자리 맞춰봐: ")
    strike = 0
    ball = 0

    #strike, ball 판정하자
    for i in range(len(computer)):
        for j in range(len(player)):
            if computer[i] == player[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    print("{}\tstrike:{}\tball:{}".format(player,strike,ball))
    # print(player, "strike: ", strike, "ball: ", ball)

    if computer == player:
        print("HIT")
        break
