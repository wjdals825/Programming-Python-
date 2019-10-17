#p239
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름: "+ self.name+"\n나이: " +str(self.age))

p = Person("장원이", 18)

f = open("person_data.bin", "wb")
pickle.dump(p, f)       #p객체를 f파일로 저장
f.close()

#load
#p247
f = open("person_data.bin", "rb")
person1 = pickle.load(f)
f.close()
print(person1)

#save object list
#p240
p1 = Person("이은상", 18)
p2 = Person("김재환", 24)
p3 = Person("박지민", 25)
people = [p1, p2, p3]
f = open("people_data.bin", "wb")
pickle.dump(people, f)
f.close()

#load obhect list
#p247
f = open("people_data.bin", "rb")
p.o = pickle.load(f)
f.close()
# print(p.o)
for p in p.o:
    print(p)

sum = 0
for p in p.o:
    sum += p.age
print(sum)

# person2 = Person("임정훈", 40)
# f = open("savefile.per", "w", encoding="utf-8")
# f.write(person2.name)
# f.write("\t")
# f.write(person2.age)
# f.write("\n")
# f.close()
