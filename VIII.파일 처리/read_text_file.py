f = open("file.txt","r", encoding="utf-8")            #r : read text

text = f.read()
print(text)

f.close()

#한줄씩 읽어오자
f = open("file.txt","r", encoding="utf-8")            #r : read text

text0 = f.readline()
print(text0)
text1 = f.readline()
print(text1)


f.close()