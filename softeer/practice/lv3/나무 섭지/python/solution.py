import sys

n,m = map(int, sys.stdin.readline().split())
mx = [-1, 0, 1, 0]
my = [0, 1, 0, -1]
grid = []
users = []
destinationLoc = []
ghosts = []
userVisited = []
ghostVisited = []
for x in range(n):
    gridRow = list(sys.stdin.readline().strip());
    grid.append(gridRow)
    userVisited.append([0]*m)
    ghostVisited.append([0]*m)
    # N: 남우, D: 출구, G: 유령, #: 벽, .: 비어있는 칸
    if len(users) == 0 and "N" in gridRow:
        # 유저인 남우는 한명
        y = gridRow.index("N")
        users.append([x, y])
        userVisited[x][y] = 1
    if len(destinationLoc) == 0 and "D" in gridRow:
        # 출구는 한곳
        y = gridRow.index("D")
        destinationLoc = [x, y]
    if "G" in gridRow:
        # 유령은 여럿일 수 있다.
        for y, v in enumerate(gridRow):
            if v == "G":
                ghosts.append([x, y])
                ghostVisited[x][y] = 1

#targets가 모든 거리까지 걸리는 시간을 visited에 입력한다.
def bfs(targets, visited, fixedAvoid=[], visitedAvoid=[]):
    while len(targets) != 0:
        x, y = targets.pop(0)
        for i in range(4):
            nx=x+mx[i]
            ny=y+my[i]
            #다음 위치가 격자를 벗어나거나, fixedAvoid 식별자를 가진 곳으로는 가지 않게한다.
            if nx<0 or nx>=n or ny<0 or ny>=m or grid[nx][ny] in fixedAvoid:
                continue
            nVisitValue = visited[x][y] +1
            #다음 위치 비용이 설정전이면서
            #다음 위치의 예상비용이 해당 위치에서 visitedAvoid의 비용보다 작을 경우(보다 빨리 도착할 수 있는 경우)
            #다음 위치의 비용을 설정하고 더 진행이 가능하므로 target을 복구한다.
            if visited[nx][ny]==0 and (len(visitedAvoid)==0 or nVisitValue<visitedAvoid[nx][ny]):
                visited[nx][ny]=nVisitValue
                if nx == destinationLoc[0] and ny == destinationLoc[1]:
                    continue
                targets.append([nx,ny])

ghosts.sort(key=lambda ghost:
                        abs(destinationLoc[0] - ghost[0]) + abs(destinationLoc[1] - ghost[1]))
bfs([ghosts[0]], ghostVisited)
bfs(users, userVisited, ['#'], ghostVisited)
print("No" if userVisited[destinationLoc[0]][destinationLoc[1]]==0 else "Yes")
