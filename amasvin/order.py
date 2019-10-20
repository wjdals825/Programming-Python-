#order.py
from coffee import Coffee
from bubbletea import Bubbletea

class Order:
  def __init__(self):
    self.order_menu = []

  def show_menu(self):
    print("0:아메리카노 1800원, 1:딸기요거트 3500원")

  def order_drink(self):
    #반복↓
    while True:
      #1. show menu
      self.show_menu()

      #2. 주문받자. 음료선택하자
      order = input("무엇을 고르시겠습니까? ")
      if order == "":
        break
      # _drinks = [Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500)]
      # drink = _drinks[int(order)]
      if int(order) == 0:
        drink = Coffee("아메리카노", 1800)
      elif int(order) == 1:
        drink = Bubbletea("딸기요거트", 3500)
      #3. 음료 옵션선택하자
      drink.order()

      self.order_menu.append(drink)
    #반복↑
    #4. 주문한 음료 내용 보여주자
    for d in self.order_menu:
      print(d)
    #5. 합계 금액 보여주자
    print("총금액: "+str(self.sum_price())+"원")
  
  def sum_price(self):
    sum = 0
    for d in self.order_menu:
      sum += d.price

    return sum