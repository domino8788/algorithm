function repeatCount(s, repeatS) {
  let startIndex = 0;
  let count = 1;
  while (s.slice(startIndex).indexOf(repeatS) === 0) {
    count++;
    startIndex += repeatS.length;
  }
  return [count, startIndex];
}

function compression(s, nod) {
  let compressResult = '';
  let before = s.slice(0, nod);
  let after = s.slice(nod);
  do {
    const [count, nextIndex] = repeatCount(after, before);
    compressResult = compressResult.concat(`${count === 1 ? '' : count}${before}`);
    before = after.slice(nextIndex, nextIndex + nod);
    after = after.slice(nextIndex + nod);
  } while (after.length !== 0);
  compressResult = compressResult.concat(before);
  return compressResult;
}

function solution(s) {
  let nod = s.length !== 1 ? Math.floor(s.length / 2) : 1;
  const lengthArray = [];
  while (nod !== 0) {
    lengthArray.push(compression(s, nod--).length);
  }
  return Math.min(...lengthArray);
}

const assert = require('assert');

assert(solution('aabbaccc') === 7);
assert(solution('ababcdcdababcdcd') === 9);
assert(solution('abcabcdede') === 8);
assert(solution('abcabcabcabcdededededede') === 14);
assert(solution('xababcdcdababcdcd') === 17);
console.log('all test pass');
