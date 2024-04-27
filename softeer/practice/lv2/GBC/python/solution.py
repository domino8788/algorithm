import sys

N, M = map(int, sys.stdin.readline().split())
sections = []
limits = []

for i in range(N):
    section, limit = map(int, sys.stdin.readline().split())
    sections.append(section)
    limits.append(limit)
    
sectionIdx = 0 #현재 테스트하고 있는 구역의 index
maxExceed = 0 #제한 속도를 가장 크게 벗어난 값
testTopFloor = 0 #테스트 하려는 구간의 가장 위층
sectionTopFloor = sections[sectionIdx] #현재 테스트하고 있는 구역의 가장 위층

for i in range(M):
    goUpFloor, speed = map(int, sys.stdin.readline().split())
    testTopFloor += goUpFloor
    while testTopFloor > sectionTopFloor:
        exceed = speed - limits[sectionIdx];
        if maxExceed < exceed: maxExceed = exceed
        if N > sectionIdx+1:
            sectionIdx+=1   
            sectionTopFloor+=sections[sectionIdx]
    exceed = speed - limits[sectionIdx];
    if maxExceed < exceed: maxExceed = exceed
    if testTopFloor == sectionTopFloor and N > sectionIdx+1:
        sectionIdx+=1
        sectionTopFloor+=sections[sectionIdx]

print(maxExceed)