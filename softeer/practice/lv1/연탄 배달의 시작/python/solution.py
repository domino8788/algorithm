import sys

townCount = int(input())
townPositions = list(map(int, input().split()))
distances = {}
for i in range(townCount-1):
    distance = townPositions[i+1]-townPositions[i]
    distances[distance] = distances[distance] + 1 if distance in distances else 1

print(distances[min(distances.keys())])