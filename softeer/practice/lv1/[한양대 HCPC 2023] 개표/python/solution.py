import sys

candidateCount = int(input())
vote1="|"
vote5="++++"
for i in range(candidateCount):
    votes = int(input())
    vote5Count, vote1Count = divmod(votes, 5);
    result = ((vote5 + " ") * (vote5Count-1)) + (vote5 + (" " if vote1Count > 0 else "") if vote5Count > 0 else "") + vote1*vote1Count
    print(result)
