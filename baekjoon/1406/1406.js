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
  const [prev, after] = cmds.reduce(
    ([prev, after], cmd) => {
      switch (cmd[0]) {
        case 'L':
          if (prev.length) after.push(prev.pop());
          break;
        case 'D':
          if (after.length) prev.push(after.pop());
          break;
        case 'B':
          prev.pop();
          break;
        case 'P':
          prev.push(cmd[2]);
          break;
      }
      return [prev, after];
    },
    [[...str], []]
  );
  console.log([...prev, ...after.reverse()].join(''));
  process.exit();
});
