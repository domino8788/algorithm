## 금고털이
> https://softeer.ai/practice/6288

## 평가
### 2024-04-24
```
한정된 자원 내에서 가장 큰 가치를 계산하는 문제
한정된 자원인 가방의 수용량 내에서
가장 비싼(가치 있는) 순으로 금속을 담으면 된다.

map에 무게당 가격을 key로 금속의 무게를 배열에 누적시킨 후
가방의 수용량이 0이 될 때까지 순회하면서
무게 당 가격(key)값이 가장 큰 금속(value)들을 담으면 된다.
```