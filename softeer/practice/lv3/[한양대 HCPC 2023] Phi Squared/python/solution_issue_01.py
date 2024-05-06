import sys

# N: 미생물의 수
N = int(sys.stdin.readline().strip())
microbes = list(
    map(lambda x: (x[0] + 1, int(x[1])), enumerate(sys.stdin.readline().split()))
)
mergeMicrobeIdx = 0
while len(microbes) != 1:
    microbe = microbes[mergeMicrobeIdx]
    leftMicrobeIdx = mergeMicrobeIdx - 1
    rightMicrobeIdx = mergeMicrobeIdx + 1
    if (
        leftMicrobeIdx >= 0
        and microbes[leftMicrobeIdx][1] <= microbe[1]
        and rightMicrobeIdx < len(microbes)
        and microbes[rightMicrobeIdx][1] <= microbe[1]
    ):
        mergeMicrobes = [
            microbes.pop(leftMicrobeIdx),
            microbes.pop(leftMicrobeIdx),
            microbes.pop(leftMicrobeIdx),
        ]
        microbe = (
            microbe[0],
            mergeMicrobes[0][1] + mergeMicrobes[1][1] + mergeMicrobes[2][1],
        )
        microbes.insert(leftMicrobeIdx, microbe)
        mergeMicrobeIdx -= 1
    elif leftMicrobeIdx >= 0 and microbes[leftMicrobeIdx][1] <= microbe[1]:
        mergeMicrobes = [microbes.pop(leftMicrobeIdx), microbes.pop(leftMicrobeIdx)]
        microbe = (microbe[0], mergeMicrobes[0][1] + mergeMicrobes[1][1])
        microbes.insert(leftMicrobeIdx, microbe)
        mergeMicrobeIdx -= 1
    elif rightMicrobeIdx < len(microbes) and microbes[rightMicrobeIdx][1] <= microbe[1]:
        mergeMicrobes = [microbes.pop(mergeMicrobeIdx), microbes.pop(mergeMicrobeIdx)]
        microbe = (microbe[0], mergeMicrobes[0][1] + mergeMicrobes[1][1])
        microbes.insert(mergeMicrobeIdx, microbe)
    if mergeMicrobeIdx == len(microbes) - 1:
        mergeMicrobeIdx = 0
    else:
        mergeMicrobeIdx += 1
print(microbes[0][1])
print(microbes[0][0])
