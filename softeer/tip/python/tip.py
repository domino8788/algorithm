import sys

#입력을 받을 때는 input() 보다 sys.stdin.readline()을 이용하는게 부하가 적다.
#단, sys.stdin.readline()은 \n까지 입력 받으므로 이를 제거하기위해 strip()를 호출한다. 
n = sys.stdin.readline().strip()

#입력을 공백 단위로 나눠서 int로 변환하고 구조분해할당한다.
input1, input2 = map(int, sys.stdin.readline().split())

#map 함수는 map객체를 반환하므로 list로 쓰고싶다면 list()로 감싸야한다.
arrayInput = list(map(int, sys.stdin.readline().split()))

#list를 구조분해할당 하는 방법. iterable한 요소는 동일하게 적용 가능하다.
a, *mid, b = [1,2,3,4,5,6] #a=1, mid=[2,3,4,5], b=6
a,b,c = [1,2,3] #왼쪽 변수와 오른쪽 값 할당하는 부분의 구조는 동일해야한다. ex) a,b,c = [1,[2,3]] 는 error
