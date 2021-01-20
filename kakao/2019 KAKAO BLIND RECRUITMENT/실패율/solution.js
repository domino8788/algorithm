function solution(N, stages) {
  return Array(N)
    .fill()
    .map((_, i) => {
      const challengers = stages.filter(s => s > i);
      const failures = challengers.filter(s => s === i + 1);
      const failureRate = failures.length / challengers.length;
      return [i + 1, failureRate ? failureRate : 0];
    })
    .sort(([, a], [, b]) => (a <= b ? 1 : -1))
    .map(([sn]) => sn);
}
