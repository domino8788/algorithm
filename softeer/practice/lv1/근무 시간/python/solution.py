import sys

total = 0;
for i in range(5):
    start, end = input().split()
    startHour, startMinutes = map(int, start.split(":"))
    endHour, endMinutes = map(int, end.split(":"))
    total += (endHour - startHour)*60+(endMinutes - startMinutes)

print(total)