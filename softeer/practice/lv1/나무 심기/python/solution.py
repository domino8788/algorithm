import sys

n = int(input())
f = sorted(map(int, input().split()));
print(max(f[0] * f[1], f[-1] * f[-2]))