import sys

n,m = map(int, sys.stdin.readline().split()) #n: 땅 크기 n*n, m: 친구들 수
dx = [-1, 0, 1, 0] #상하좌우 이동 시 x축 가산
dy = [0, 1, 0, -1] #상하좌우 이동 시 y축 가산
grid = [] #땅
friends = [] #친구들 위치
totalHarvest = 0 #전체 수확량

for i in range(n): #격자모양 땅에 수확 정보 추가
    grid.append(list(map(int, sys.stdin.readline().split()))) 
    
for i in range(m): #친구들 위치 정보 및 초기 위치 수확량을 전체 수확량에 가산
    loc = [int(x) - 1 for x in map(int, sys.stdin.readline().split())]
    cx, cy = loc[0], loc[1]
    friends.append(loc)
    totalHarvest += grid[cx][cy]
    grid[cx][cy] = 0

def tic(currentLoc, currentFriendIdx, sec, harvest): #tic, 1초가 흐를 동안 발생하는 동작을 함수화
    global totalHarvest
    global grid
    if sec == 3: #3초가 흘렀으므로 중단점 설정
        if currentFriendIdx < m-1: #아직 다 움직이지 않은 친구가 있을 경우
            tic(friends[currentFriendIdx+1], currentFriendIdx+1, 0, harvest) #다음 친구가 수확을 위해 이동
        elif totalHarvest < harvest: # 기존 전체 수확량 보다 현재 케이스의 수확량이 더 많은 경우 대체한다.
            totalHarvest = harvest
        return #재귀 중단
    for i in range(4): #상,하,좌,우
        nx = currentLoc[0]+dx[i] #다음 x축 위치
        ny = currentLoc[1]+dy[i] #다음 y축 위치
        if nx<0 or nx>=n or ny<0 or ny>=n: continue #다음 위치가 격자를 벗어나면 continue
        tmp = grid[nx][ny] #다음 위치의 수확량 임시저장 
        grid[nx][ny] = 0 #다음 위치 수확처리
        tic([nx, ny], currentFriendIdx, sec+1, harvest + tmp) #다음 위치와 수확정보로 1초가 흐르게 함수 호출
        grid[nx][ny] = tmp #다른 방향 이동을 고려해 기존 방향 이동 시의 수확량을 복구
    
tic(friends[0], 0, 0, totalHarvest) #첫번째 친구가 0초부터 수확 시작
print(totalHarvest)