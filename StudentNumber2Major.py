#학번 입력받아
#학과 출력하기

#print("학번을 입력해주세요.:")
#num=(input())
#x=num[0:2]
#if x == "11" or "12" or "21" or "22" :
    #print("뉴미디어소프트웨어과") 
#elif x == "13" or "14" or "23" or "24" :
    #print("뉴미디어웹솔루션과")
#elif x == "15" or "16" or "25" or "26" :
    #print("뉴미디어디자인과")
#elif x == "31" or "32" :
    #print("인터랙티브미디어과")
#elif x == "33" or "34" :
    #print("뉴미디어디자인과")
#elif x == "35" or "36" :
    #print("뉴미디어솔루션과")

student_number = (input())

grade = student_number[0]
classroom = student_number[1]
if grade == "1" or grade == "2":
    if classroom == "1" or classroom == "2":
        print("뉴미디어소프트웨어과")
    elif classroom == "3" or classroom == "4":
        print("뉴미디어웹솔루션과")
    elif classroom == "5" or classroom == "6":
        print("뉴미디어디자인과")
elif grade == 3 :
    if classroom == "1" or classroom == "2":
        print("인터랙티브미디어과")
    elif classroom == "3" or classroom == "4":
        print("뉴미디어디자인과")
    elif classroom == "5" or classroom == "6":
        print("뉴미디어솔루션과")

