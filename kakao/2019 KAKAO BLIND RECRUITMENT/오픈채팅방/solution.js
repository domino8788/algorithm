function solution(record) {
  const typeMap = {Enter: '님이 들어왔습니다.', Leave: '님이 나갔습니다.'};
  const logs = [];
  const userInfo = record.reduce((_userInfo, _record) => {
    const [type, id, nick] = _record.split(' ');
    if (type === 'Enter' || type === 'Change') _userInfo[id] = nick;
    if (type === 'Enter' || type === 'Leave') logs.push({id, type});
    return _userInfo;
  }, {});
  return logs.map(log => `${userInfo[log.id]}${typeMap[log.type]}`);
}

const assert = require('assert');

const record = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan'];
const result = ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.'];
assert(JSON.stringify(solution(record)) === JSON.stringify(result));
console.log('all test pass');
