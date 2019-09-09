from datetime import datetime

print('현재 날짜 시각 객체 얻기')
today = datetime.now()
print('today = datetime.now() : ', today)
print('년 월 일 : today.year, today.month, today.day', today.year, today.month, today.day)
print('시 분 초 : today.hour, today.minute, today.second', today.hour, today.minute, today.second)
print('요일 : ', today.weekday())
day = datetime(2019, 1, 1, 0, 0, 0,)
print('day = datetime(2019, 1, 1, 0, 0, 0, ) : ', day)
print('2019년부터 지나온 시간 구하기')
print('today - day : ', today - day)

#내가 태어난 날은 무슨 요일?
birthday = datetime(2002, 8, 25)
print("월화수목금토일"[birthday.weekday()], "요일")

#나는 며칠 살았을까?
day = datetime(1977,9,30)
print(today - birthday)
print(today - day)

#올해 크리스마스 며칠 남았을까?
christmas = datetime(2019, 12, 25)
print(today - christmas)