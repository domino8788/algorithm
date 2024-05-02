import sys

houseCount = int(input())
radiuses = list(map(int, input().split()))

divisorDic={}

for radius in radiuses:
    for i in range(2, radius+1):
        divisor = radius%i
        if divisor == 0:
            if i in divisorDic:
                divisorDic[i] += 1
            else:
                divisorDic[i] = 1
print(max(divisorDic.values()))