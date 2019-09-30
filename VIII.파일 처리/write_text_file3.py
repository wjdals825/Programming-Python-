fi = open("test.ama", "w", encoding="utf-8")
fi.write("아이스아메리카노\t2800\t레귤러\t100%\t50%\t코코\n")
fi.write("오레오쉐이크\t3500\t점보\t50%\t150%\t타피오카\n")
fi.write("딸기코코넛\t3800\t점보\t0%\t150%\t알로에\n")
fi.close()

fi = open("test.ama", "r", encoding="utf-8")
sum = 0
while True:
    data = fi.readline()
    if not data:
        break
    l = data.split("\t")           # 화이트스페이스(띄어쓰기, \t, \n 등)로 분리
    # print (l[1]+"원")
    sum += int(l[1])
fi.close()
print("주문한 총금액: "+str(sum)+"원")