majors= [["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],["인터랙티브미디어과","뉴미디어디자인과","뉴미디어솔루션과"]]

student_number = input("힉번을 입력하세요 : ")

grade= int(student_number[0])
classroom= int(student_number[1])
print(majors[grade-1][(classroom-1)//2])