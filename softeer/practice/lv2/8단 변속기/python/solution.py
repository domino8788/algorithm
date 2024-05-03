import sys

numbers = list(map(int, sys.stdin.readline().split()))
result = None

for i in range(len(numbers)-1):
    checkStatus = None
    if numbers[i] < numbers[i+1]:
        checkStatus = "ascending"
    elif numbers[i] > numbers[i+1]:
        checkStatus = "descending"
    if checkStatus != None and result != None and result != checkStatus:
        result = "mixed"
        break
    result = checkStatus
print(result)