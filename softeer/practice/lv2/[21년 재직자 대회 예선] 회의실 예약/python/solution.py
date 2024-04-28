import sys

testCaseCount = int(sys.stdin.readline())


# numberBulbs = [
#     [1,1,1,0,1,1,1],
#     [0,0,1,0,0,1,0],
#     [1,0,1,1,1,0,1],
#     [1,0,1,1,0,1,1],
#     [0,1,1,1,0,1,0],
#     [1,1,0,1,0,1,1],
#     [1,1,0,1,1,1,1],
#     [1,1,1,0,0,1,0],
#     [1,1,1,1,1,1,1],
#     [1,1,1,1,0,1,1]
# ]
# 각 숫자별 전구상태(1:켜짐, 0:꺼짐)를 이진수로 표현
numberBulbs = [
    0b1110111,
    0b0010010,
    0b1011101,
    0b1011011,
    0b0111010,
    0b1101011,
    0b1101111,
    0b1110010,
    0b1111111,
    0b1111011
]

for i in range(testCaseCount):
    testCase1, testCase2 = map(int, sys.stdin.readline().split()) #테스트 케이스 숫자 둘
    largeTestCase = str(max(testCase1, testCase2))[::-1] #테스트 케이스 중 큰 숫자를 문자열로 변환해서 역순정렬
    smallTestCase = str(min(testCase1, testCase2))[::-1] #테스트 케이스 중 작은 숫자를 문자열로 변환해서 역순정렬
    clickCount = 0 # 스위치를 누른 횟수
    for j, num in enumerate(largeTestCase):
        if len(smallTestCase) > j: #대조해야할 자리수가 작은 숫자의 최대길이보다 작을 경우 
            largeTestCaseBulb = numberBulbs[int(num)]
            smallTestCaseBulb = numberBulbs[int(smallTestCase[j])]
            clickCount += bin(largeTestCaseBulb^smallTestCaseBulb).count("1") # xor 연산하면 전구위치간 상태가 다를 경우 1로 연산됨, 결과의 1을 세면 스위치를 눌러야하는 횟수다.
        else: #대조해야할 자리수가 작은 숫자의 최대길이보다 클 경우
            clickCount += bin(numberBulbs[int(num)]).count("1") #켜야하는(1) 전구의 수만 가산한다.
            
    print(clickCount)