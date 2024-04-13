#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;

  for (let i = 0; i < (len / 2); i++) {
    [list[i], list[len - (i + 1)]] = [list[len - (i + 1)], list[i]];
  }

  return list;
};
