sum = 0
for i in range(1, 50, 1):
    sum += i
    if sum > 100:
        break;
sum -= i
print("%d" %sum)
print("-------")

sum, i = 0, 1
j = int(input("숫자를 입력합니다. "))
while True:
    if i <= j:
        sum += i
        i += 1
    elif j < i:
        break;
print("1에서 %d까지의 합은 %d입니다." %(j, sum))