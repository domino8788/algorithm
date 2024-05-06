import sys
from collections import deque

# N: 미생물의 수
N = int(sys.stdin.readline().strip())
# 흡수 전 미생물
microbes = deque(
    list(map(lambda x: (x[0] + 1, int(x[1])), enumerate(sys.stdin.readline().split())))
)
# 흡수 후 미생물
mergedMicrobes = deque()

# 흡수전 미생물이 하나만 남고 흡수후 미생물이 없을 경우가 아니면 반복한다.
while not (len(microbes) == 1 and len(mergedMicrobes) == 0):
    # 흡수를 시도하는 미생물
    microbe = microbes.popleft()
    # 흡수를 시도하는 미생물의 좌측 미생물
    leftMicrobe = mergedMicrobes.pop() if len(mergedMicrobes) > 0 else None
    # 흡수를 시도하는 미생물의 우측 미생물
    rightMicrobe = microbes.popleft() if len(microbes) > 0 else None
    mergedMicrobe = microbe
    # 좌측 미생물이 있으면 작거나 같은지 체크 후 흡수한다. 아니면 큐에 반환한다.
    if leftMicrobe is not None:
        if leftMicrobe[1] <= microbe[1]:
            mergedMicrobe = (microbe[0], microbe[1] + leftMicrobe[1])
        else:
            mergedMicrobes.append(leftMicrobe)
    # 우측 미생물이 있으면 작거나 같은지 체크 후 흡수한다. 아니면 큐에 반환한다.
    if rightMicrobe is not None:
        if rightMicrobe[1] <= microbe[1]:
            mergedMicrobe = (microbe[0], mergedMicrobe[1] + rightMicrobe[1])
        else:
            microbes.appendleft(rightMicrobe)
    # 병합된 미생물을 큐에 넣는다.
    mergedMicrobes.append(mergedMicrobe)
    # 병합전 미생물이 빌 경우 하루가 지났다는 의미이므로 큐를 바꿔준다.
    if len(microbes) == 0:
        microbes = mergedMicrobes
        mergedMicrobes = deque()

lastMicrobe = microbes.pop()
print(lastMicrobe[1])
print(lastMicrobe[0])
