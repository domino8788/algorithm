## 함께하는 효도
> https://softeer.ai/practice/7727

## 평가
### 2024-04-23
```
DFS 변형 문제
단순히 재귀함수를 이용해 DFS를 구현하는게 아니며
1depth가 1초라 치고 모든 친구들이 1초 동안 동시에 움직임을 고려해야한다.

즉 친구들의 수 만큼 DFS를 스레드로 병행하는 느낌인데
기존에 수확한 곳은 수확량이 0이 되므로 동기화도 고려해야한다.

그렇다고 진짜 스레드로 구현할건 아니고
한 친구의 동작이 끝나면
다음 친구가 기존에 수확된 땅을 기준으로
최대치로 수확할 수 있는 방향을 탐색하면 된다.

단, 3초 이동한 모든 케이스를 다 고려하기 전까진
현재까지 이동한 방향이 최대 수확량을 가진다는 보장이 없으므로
재귀가 돌아가면서 다른 방향으로 이동한 케이스를 고려할 때
이전에 이동하면서 수확한 땅을 복구해야한다.

이는 다음에 수확할 땅의 수확량을 보존하고
다음 땅을 수확했다는 가정하에 재귀함수를 진행시키되
재귀가 끝나면 그 땅의 수확량을 복구하면 된다.
ex)
grid[nx][ny] = 0 #다음 위치 수확처리
tic([nx, ny], currentFriendIdx, sec+1, harvest + tmp) #다음 위치와 수확정보로 1초가 흐르게 함수 호출
grid[nx][ny] = tmp #다른 방향 이동을 고려해 기존 방향 이동 시의 수확량을 복구

뭔가.. 머리속으로 해결책은 그려지는데 로직으로는 잘 안풀린 문제였다.
근데 계속 고민하면서 개선하니까 나름 간결하게 풀리는 구석도 있었다.
처음엔 상하좌우 이동하는 로직을 if문 덕지덕지 붙여서 복잡하게 구성했는데
상하좌우 기준으로 x축, y축 가산치를 배열로 정의하니까
그 복잡하던 로직이 단 몇줄로 간결하게 정리되었다.

이런 문제를 풀면서 얻은 노하우는 이곳저곳 써먹을 수 있을듯 싶다.
```