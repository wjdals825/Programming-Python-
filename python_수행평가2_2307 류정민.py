#2307_류정민 
#컴퓨터에서 랜덤으로 주문을 받아 와플을 만드는 게임

print ("Ꮚ •ꈊ•Ꮚ  (??)")
print ("------------------------------")
print ("어! 안녕하세요~ 오늘 저와 함께할 일일 사장님이 오신다고 했는데...\n맞으신가요?\n")

answer = input ("Press Enter")
if answer == "":
    print ("\n\n(*´∀｀） (나)")
    print ("------------------------------")
    print ("아, 저 맞아요!!\n")

answer1 = input ("Press Enter")
if answer1 == "":
    print ("\n\nᏊ ❛ꈊ❛Ꮚ  (양양)")
    print ("------------------------------")
    print ("안녕하세요! 저는 사장님께 일을 알려드릴 양양이라고 합니다\n만나서 반가워요!\n")

answer2 = input ("Press Enter")
if answer2 =="":
    print ("\n\n(*´∀｀） (나)")
    print ("------------------------------")
    print ("네 잘부탁드려요~^ㅁ^\n")

class random_money:
        point = 0
        import random
        money = ['1만원','2만원', '3만원', '4만원','5만원']
        money_order = random.choice(money)
        answer3 = input ("Press Enter")

    # while point < money_order:
        if answer3 =="":
            print ("\n\nᏊ ❛ꈊ❛Ꮚ  (양양)")
            print ("------------------------------")
            print ("\n\n저희 와플러는 고객님이 주문하시는 메뉴에 맞춰 와플을 만드는 가게입니다 \n저희 와플러의 와플은 각자의 취향에 따라 주문을 받습니다."\
                "\n\n반죽 불 세기, 반죽 굽는 시간, 크림의 종류, 시럽 총 4가지를 각자의 취향에 맞춰 주문을 할 수 있습니다."\
                "\n저희는 주문을 기억하여 주문에 맞춰 와플을 만들면 된답니다!! \n\n오늘의 목표 금액을 달성하였을시에 자동으로 오늘의 장사는 끝이 난답니다!"\
                "\n잘 이해가 되셨나요?")

        answer12 = input ("Press Enter")
        if answer12 == "":
            print ("\n\n\n그럼 바로 시작해볼까요 \n\n 3\n\n 2\n\n 1\n\n START!  ")
            print (" \n DAY1 \n ================================== \n 오늘의 목표 금액은",money_order+"입니다.\n 목표 금액 달성까지 힘내봐요!!\n"\
                " ==================================")

        answer4 = input ("\n\nPress Enter")
        if answer4 =="":

            #주문자
            man = ['( ๑ò ᆺ  ó๑)', 'ʕ　·ᴥ·ʔ', '٩(●ᴗ●)۶', 'Ⴚ ტ ◕ ‿ ◕ ტ Ⴢ', '(◕ ▿ ◕ ✿)']
            # 반죽 불 세기 조절 (1~5)
            fire = ['1단계', '2단계', '3단계', '4단계', '5단계']
            # 반죽 굽는 시간 선택 (5~20분)
            time = ['5분', '10분', '15분', '20분']
            # 주문에 맞는 생크림 선택 (3종 중 택 1)
            cream = ['딸기크림', '초코크림', '생크림']
            # 주문에 맞는 시럽 선택 (4종 중 택 1)
            syrup = ['사과시럽', '바나나시럽', '초코시럽', '딸기시럽']
            # 후기
            log = ['美味 (미미)!!','오우~ 제가 먹어본 와플 중 최고인거 같아요','별이 다섯개~','둘이 먹다 하나가 죽어도 모를 맛이네요 ㅎㅎ']
            blog = ['으엑, 이 와플에 대한 어떠한 코멘드도 사치인거 같네요.','아...어...네...먹을만 하네요..','오우~ 올해 최고의 돈낭비~']

            man_order = random.choice(man)
            fire_order = random.choice(fire)
            time_order = random.choice(time)
            cream_order = random.choice(cream)
            syrup_order = random.choice(syrup)
            log_order = random.choice(log)
            blog_order = random.choice(blog)

            print ("\n\n\n",man_order,'\n------------------------------\n반죽 불 세기는',fire_order+'로 해주시고요, 반죽 굽는시간은',time_order+\
                '으로 해주세요.\n그리고 크림은',cream_order+'으로 해주시고, 마지막으로 시럽은', syrup_order +'으로 해주세요')
            
            check = input ("\n\nᏊ •ꈊ•Ꮚ\n------------------------------\n주문 들어왔어요~ \n확인 하셨으면 enter키를 눌러주세요!")

            if check == '':
                print ('\n 10 \n\n 9 \n\n 8 \n\n 7 \n\n 6 \n\n 5 \n\n 4 \n\n 3 \n\n 2 \n\n 1 \nSTART\n\n')
            else :
                print ('Enter 키를 눌러주세요.')
        
            point = 0

            answer5 = input ("와플 반죽 불 세기는? [1단계, 2단계, 3단계, 4단계, 5단계] (단어로 작성해주세요!)\n->")
            answer6 = input ("와플 반죽 굽는 시간은 ? [5분, 10분, 15분, 20분] (단어로 작성해주세요!)\n->")
            answer7 = input ("크림의 종류는? [딸기크림, 초코크림, 생크림] (단어로 작성해주세요!)\n->")
            answer8 = input ("시럽의 종류는? [사과시럽, 바나나시럽, 초코시럽, 딸기시럽] (단어로 작성해주세요!)\n->")
            
            if answer5 == fire_order :
                point += 1000
            else :
                point += 500
            
            if answer6 == time_order :
                point += 1000
            else : 
                point += 500

            if answer7 == cream_order :
                point += 1000
            else :
                point += 500

            if answer8 == syrup_order :
                point += 1000
            else :
                point += 500
            
            if point >=3000:
                print (man_order+"\n-----------------------------\n",log_order)
            else :
                print (man_order+"\n-----------------------------\n",blog_order)
            print ("\n\n\n\n현재 수익 \n=============================\n")
            print (point)
            print ("\n=============================\n")

        # if point >= money_order :
        #     break




# 주문에 맞는 와플 만들었을 시 랜덤으로 맛 평가 출력 (5종 중 랜덤)
# 주문에 맞는 와플 실패했을 시 랜덤으로 맛 평가 출력 (5종 중 랜덤)
# 한문제 당 10점으로 치환해서 100점을 만들면 게임 종료 x
# 목표 금액 랜덤으로 나오고 목표금액 달성시 게임 종료 왜 에러나ㅜㅜㅜㅜㅛㅜㅜ
# 기회 3번을 주고 3번을 다 실패할시 현재 점수를 알려주고 게임 종료.
# 생각하기 ! 실패 성공 확인 어케?
# 주문마다 일련번호를 넣어서 확인..?