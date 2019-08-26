student_number = (input())

grade = student_number[0]
classroom = student_number[1]
num = student_number[2:4]

if grade == "1" or grade == "2":
    if classroom == "1" or classroom == "2":
        print(grade+"학년","뉴미디어소프트웨어과",classroom+"반",num+"번입니다.")
    elif classroom == "3" or classroom == "4":
        print(grade+"학년","뉴미디어웹솔루션과",classroom+"반",num+"번입니다.")
    elif classroom == "5" or classroom == "6":
        print(grade+"학년","뉴미디어디자인과",classroom+"반",num+"번입니다.")
elif grade == "3" :
    if classroom == "1" or classroom == "2":
        print(grade+"학년","인터랙티브미디어과",classroom+"반",num+"번입니다.")
    elif classroom == "3" or classroom == "4":
        print(grade+"학년","뉴미디어디자인과",classroom+"반",num+"번입니다.")
    elif classroom == "5" or classroom == "6":
        print(grade+"학년","뉴미디어솔루션과",classroom+"반",num+"번입니다.")

