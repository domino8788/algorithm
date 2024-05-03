import sys

K, P, N = map(int, sys.stdin.readline().split())
result = K
for i in range(N):
    result = result*P%1000000007
print(result)