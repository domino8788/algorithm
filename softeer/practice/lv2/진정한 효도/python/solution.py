import sys

minCost=None
field=[]
for i in range(3):
    field.append(list(map(int, sys.stdin.readline().split())));

#매개변수로 받은 row를 평준화 하는데 드는 비용을 계산하는 함수
def getCost(row):
    return max(row) - min(row)
    
#cost가 minCost인지 검토하고 맞으면 주입하는 함수
def checkMinCost(cost):
    if cost==0:
        print(cost)
        exit()
    else:
        global minCost
        if minCost == None or minCost > cost:
            minCost = cost

#가로 평준화 비용 체크
for i in range(3):
    checkMinCost(getCost(field[i]))
#가로 평준화에서 최저값(0)이 나오지 않았다면 세로 평준화 비용 체크
if minCost != 0:
    for i in range(3):
        checkMinCost(getCost([field[0][i], field[1][i], field[2][i]]))

print(minCost)