import sys

calcCount = int(input())

for i in range(calcCount):
    a,b = map(int, input().split())
    print("Case #"+str(i+1)+": "+str(a+b))