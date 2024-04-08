#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let occur = Number(argv[2]);
  while (occur > 0) {
    console.log('C is fun');
    occur--;
  }
}
