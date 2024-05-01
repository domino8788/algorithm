import sys

A, B = map(int, input().split())
print(str("A" if A>B else "B" if A<B else "same"))