const readline = require('readline');
const r = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inputArray = [];
r.on('line', input => {
  inputArray.push(input);
}).on('close', () => {
  const [str, _, ...cmds] = inputArray;
  const [prev, next] = cmds.reduce(
    ([prev, next], cmd) => {
      switch (cmd[0]) {
        case 'L':
          if (prev.length) next.push(prev.pop());
          break;
        case 'D':
          if (next.length) prev.push(next.pop());
          break;
        case 'B':
          prev.pop();
          break;
        case 'P':
          prev.push(cmd[2]);
          break;
      }
      return [prev, next];
    },
    [[...str], []]
  );
  console.log([...prev, ...next.reverse()].join(''));
  process.exit();
});
