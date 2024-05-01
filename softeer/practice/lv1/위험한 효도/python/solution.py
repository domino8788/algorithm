import sys

#a: 술래가 뒤돌아보는 시간
#b: 술래가 앞을보는 시간
#d: 거리
a,b,d = map(int, input().split())
aDiv, aMod = divmod(d, a)
bDiv, bMod = divmod(d, b)
#aDiv*a = 터치 전 술래가 뒤돌아보는 시간
#(aDiv if aMod!=0 else aDiv-1)*b = 술래가 뒤돌아보는 횟수 만큼 앞을 보는 시간이 발생한다.
#aMod = 술래를 터치하기전 마지막으로 소요한 시간 
#a와 b를 뒤집어서 다시한번 더 실행하면 되돌아오는데 소요되는 시간이다.
print((aDiv*a+(aDiv if aMod!=0 else aDiv-1)*b+aMod)+(bDiv*b+(bDiv if bMod!=0 else bDiv-1)*a+bMod))