import sys

M,_,_ = map(int, sys.stdin.readline().split()) 
# M: 비밀 메뉴 조작법 M 개의 정수(1<=M<=K)
# N: 버튼 조작 N개의 정수(1<=N<=K)

secretManual = list(map(int, sys.stdin.readline().split()))
input = list(map(int, sys.stdin.readline().split()))
sameCheckStartIdx = 0
sameCheckIdx = 0 #secretManual 일치율 M-1이면 성공

i = 0
while i < len(input):
    if input[i] == secretManual[sameCheckIdx]: #조작법과 연속 일치하는지 체크
        if sameCheckIdx == 0: #조작법과 첫 일치하는 index라면 실패 시 복귀할 sameCheckStartIdx를 저장한다.
            sameCheckStartIdx = i 
        sameCheckIdx+=1 #현재 조작법 입력과 일치하므로 다음 조작법을 체크하기 위해 sameCheckIdx를 증가시킨다.
        if sameCheckIdx == M: #조작법의 길이 만큼 일치하는지 확인했으면 성공이므로 중단한다.
            break
    elif sameCheckIdx != 0: # 조작법과 불일치 하므로 기존에 부분일치한 상태였다면 일치정보를 초기화하고 sameCheckStartIdx로 index를 되돌린다.
        sameCheckIdx=0
        i = sameCheckStartIdx
    i+=1


print("secret" if sameCheckIdx == M else "normal")
