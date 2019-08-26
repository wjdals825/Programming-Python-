from drink import Drink

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
