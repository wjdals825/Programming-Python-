# from repeater import repeat, once
from repeater import *

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")
repeat(s, int(n))
repeat(s)
once(s)