#아마스빈 주문앱
    #Drink <-Coffee
    #       <-Bubbletea
    #Order
    #메뉴 보여주자
    #음료주문하자
    #주문한 음료 보여주자
    #총금앱 계산하자
    # 1. 음료 이름 가격
    # 2. 컵 사이즈 레귤러 점보
    # 3. 얼음량 0,50,100,150
    # 4. 당도 0,50,100,150
    # 5. 펄 타피오카, 코코,젤리, 알로에

class Drink:
        _cups = ["레귤러","점보"]
        _ices=["0%","50%","100%","150%"]
        
        def __init__(self,name,price):
            self.name = name
            self.price = price
            self.cup = 0 #기본값
            self.ice = 2
            self.sugar=2

        def __str__(self): # 이름 : self.name \t 가격: self.price원\t 컵: self.cup
            return "이름 : "+self.name+"\t가격 : "+ str(self.price) +"원\t컵 : "\
                +Drink._cups[self.cup] +"\t 얼음량:"+Drink._ices[self.ice]+" \t 당도: "+Drink._ices[self.sugar]+" "

        def set_cup(self):
            self.cup = input("컵을 선택하세요 (0: 레귤러, 1: 점보)")
            if self.cup =="": #사용자가 엔터만 치면 기본값 0을 넣자
                self.cup = 0
            else:
                self.cup = int(self.cup)
            #점보면 +300
            if self.cup == 1:
                self.price += 300
                
        def set_ice(self):
            self.ice = input("얼음량을 선택하세요(0:0%,  1: 50% , 2: 100% , 3: 150%)")
            if self.ice =="": 
                self.ice = 0
            else:
                self.ice = int(self.ice)
        def set_sugar(self):
            self.sugar = input("당도를 선택하세요(0:0%,  1: 50% , 2: 100% , 3: 150%)")
            if self.sugar =="": 
                self.sugar = 0
            else:
                self.sugar = int(self.sugar)

        def order(self):
         self.set_cup()
         self.set_ice()
         self.set_sugar()


                  
class Coffee(Drink):
    pass  #Drink 를 상속 받은 것임
class Bubbletea(Drink):
    _pearls=["타피오카","코코","젤리","알로에"]
    def __init__(self,name,price):
        super().__init__(name,price) #부모님의 생성자를 쓸 때,
        self.pearl = 0

    def set_pearl(self):  
        self.pearl = input("펄을 선택하세요 (0:타피오카 , 1: 코코, 2: 젤리 ,3: 알로에")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)
        
    def __str__(self):
            return super().__str__() + "\t펄 :"+Bubbletea._pearls[self.pearl]
                #부모님의 기존의 함수를 불러옴
    def order(self):
        super().order()
        self.set_pearl()

class order:
    _menus = [Coffee("아메리카노",1800), Bubbletea("딸기요거트",3500)]
    def __init__(self):
        self.order_menu = []
        self.order = None
    def show_menu(self):
        print("0: 아메리카노 1800원, 1: 딸기요거트 3500원")
    def sum_price(self):
        sum=0

        for drink in self.order_menu:
            sum += drink.price

        return sum


    def order_drink(self):
        #반복
        while True:
            #메뉴보여주자
            self.show_menu()
            #주문받자
            #음료선택하자
            self.order = input("음료를 선택하세요 : ")
            #음료객체생성하자
           # Coffee("아메리카노",1800)
            #Bubbletea("딸기요거트",3500)
            if self.order == "":  #메뉴선택 안하고 그냥 엔터치면 주문 끝
                break 
            drink = order._menus[int(self.order)]
            #음료옵션정하자
            drink.order()
            #주문한 음료 리스트에 추가하자
            self.order_menu.append(drink)
            #반복
        #주문한 음료 출력하자
        for drink in self.order_menu:
            print(drink)
        #금액 합계구하자
            print("총 금액은 "+str(self.sum_price())+"원 입니다.") 

o =order()
o.order_drink()
    # 아메리카노 = Drink("아메리카노",1800)
    # 아메리카노.order()
    # print(아메리카노)   #이름 : 아메리카노 \t 가격 : 1800
    # 타로밀크티 = Bubbletea("타로버블티", 3500)
    # 타로밀크티.order()

    # print(타로밀크티)