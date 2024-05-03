import sys
#bagWeight: 배낭에 담을 수 있는 무게, n: 귀금속의 종류
bagWeight, n = map(int, sys.stdin.readline().split())
metals = {}
value = 0

for i in range(n):
    #m: 금속의 무게, p: 무게당 가격
    m, p = map(int, sys.stdin.readline().split()) 
    #금속 정보 저장, 무게당 가격(p)을 key로 금속의 무게(m)을 배열에 누적시킨다. 
    if p in metals: 
        metals[p].append(m)
    else:
        metals[p] = [m]

#가방에 더 이상 담을 수 있는 무게가 없다면 반복하지 않는다.
while(bagWeight != 0):
    #무게당 가격이 가장 비싼 값
    price = max(metals.keys())
    #무게당 가격이 가장 비싼 금속의 무게를 순회한다.
    for metalWeight in metals[price]:
        #금속의 무게가 가방에 담을 수 있는 무게보다 같거나 크다면 가치를 가산하고 중단한다.
        if metalWeight >= bagWeight:
            value +=bagWeight*price
            bagWeight = 0
            break
        #금속의 무게가 가방에 담을 수 있는 무게보다 작다면 가치를 가산하고 다음 금속을 순회한다.
        else:
            value += metalWeight*price 
            bagWeight -= metalWeight
    #기존에 무게 당 가격이 가장 비싼 금속을 모두 담았으므로 가격 대조 후보에서 제거한다.
    del metals[price]

print(value)