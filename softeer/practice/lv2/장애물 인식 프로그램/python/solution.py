import sys

n = int(sys.stdin.readline())
squareMap = []

for i in range(n):
    squareMap.append(list(map(int, list(sys.stdin.readline().strip()))))
blocks = []
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

#DFS로 인접한 블록들을 탐색
def quest(currentLoc, blockIdx):
    #현재 탐색중인 장애물 정보를 저장할 element가 없으면 삽입한다.
    if blockIdx >= len(blocks):
        blocks.append(1)
    #현재 탐색중인 장애물 정보를 저장할 element가 있다면 가산한다.
    else:
        blocks[blockIdx] += 1
    #탐색이 완료된 장애물이 재탐색되는 것을 방지하기 위해 0처리
    squareMap[currentLoc[0]][currentLoc[1]] = 0
    #시계방향으로 순회한다.
    for i in range(4):
        #다음 탐색 위치, nx:x축, ny:y축
        nx, ny = currentLoc[0] + dx[i], currentLoc[1] + dy[i]
        #다음 탐색 위치가 격자를 벗어났으면 중단한다.
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        #다음 탐색 위치에 장애물이 있으면 재귀함수로 이어서 탐색한다.
        elif squareMap[nx][ny] == 1:
            quest([nx, ny], blockIdx)

#장애물 모임 idx
blockIdx = 0
#장애물 row를 순회하며 장애물(1)이 있는지 체크하고 있으면 탐색을 시작한다.
for (i, mapRow) in enumerate(squareMap):
    rowIdx = 0
    try:
        rowIdx= mapRow.index(1)
    except:
        rowIdx = -1
    #현재 row에 장애물이 없을 때 까지 반복한다.
    while rowIdx != -1:
        quest([i, rowIdx], blockIdx)
        blockIdx+=1
        #한 row에 장애물 모임이 여럿 일을 수 있으므로 더 있는지 확인한다.
        try:
            rowIdx= mapRow.index(1)
        except:
            rowIdx = -1
            
blocks.sort()
print(len(blocks))
for block in blocks:
    print(block)