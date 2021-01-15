const readline = require('readline');
const r = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
r.on('line', input => {
  r.close();
}).on('close', () => process.exit());
