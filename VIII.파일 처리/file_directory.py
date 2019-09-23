import os
data = os.listdir("c:\\")              #.: 현재 디렉터리, ..: 상위 디렉터리
print(data)
for d in data:
    print(d)
    print("is directory?: " + str(os.path.isdir(d)))
    print("is file?: " + str(os.path.isfile(d)))