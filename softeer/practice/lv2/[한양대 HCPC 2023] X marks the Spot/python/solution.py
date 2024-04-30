import sys

puzzleCount = int(sys.stdin.readline())
puzzlePiece = []
for _ in range(puzzleCount):
    s, t = sys.stdin.readline().split()
    for (i, ch) in enumerate(s):
        if ch == 'x' or ch == 'X':
            puzzlePiece.append(t[i].upper())
            break

print("".join(puzzlePiece))