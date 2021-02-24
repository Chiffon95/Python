str="수업이 끝나간다"
i = 0
while i < 3:
    print(str)
    i += 1
print("-------")

i = int(input("반복 횟수 숫자를 입력합니다. "))
j = 0;
flag = True
while flag:
    if i <= j:
        flag = False
    else:
        print(str)
    j += 1
