import sys

stationNumber = int(input())
result = list(map(int, input().split()));
for i in range(stationNumber-1):
    stationX, stationY = map(int, input().split())
    if result[1] > stationY:
        result[0] = stationX
        result[1] = stationY

print(" ".join(map(str, result)))