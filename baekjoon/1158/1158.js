const readline = require('readline');
const r = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
r.on('line', input => {
  const [N, K] = input.split(' ').map(number => Number(number));
  const circle = Array(N)
    .fill(0)
    .map((_, index) => index + 1);
  const result = [];
  let currentIndex = K - 1;
  while (circle.length) {
    result.push(circle.splice(currentIndex, 1)[0]);
    currentIndex = (currentIndex + K - 1) % circle.length;
  }
  console.log(`<${result.join(', ')}>`);
  r.close();
}).on('close', () => process.exit());
