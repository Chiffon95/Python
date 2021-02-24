sum = 0

for i in range(1, 11, 1):
    sum += 1
print("sum : %d" %sum)
print("-------")

sum = 0
for j in range (1, 11, 1):
    if j < 10:
        print("%d + " %j, end = "")
    elif j == 10:
        print("%d = " %j, end = "")
    sum += j

print ("%d" %sum)
