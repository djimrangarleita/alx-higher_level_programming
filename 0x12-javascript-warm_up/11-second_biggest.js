#!/usr/bin/node

const { argv } = require('node:process');
const keys = [];
if (argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    keys.push(Number(argv[i]));
  }
  const sorted = keys.sort((a, b) => b - a);
  console.log(sorted[1]);
}
