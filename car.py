class Car:
    count = 0

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1                  #count만 쓰면 안 됨

    @classmethod                        #반드시 있어야함
    def get_count(cls):                 #꼭 이름이 cls 아니어도됨
        return cls.count                #Car.count 써도 됨

    def move(self):
        print(self.type + "가" + str(self.speed) + "속도로 움직입니다.")

    def speed_up(self, amount):
        self.speed += amount            #그냥 speed 쓰면 안 됨

    def speed_down(self, amount):
        self.speed -= amount


print (Car.get_count())
c = Car("스포츠카", 200)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move()

d = Car("테슬라",200)
d.speed_up(50)
d.move()
d.speed_down(150)
d.move()
print(Car.get_count())
