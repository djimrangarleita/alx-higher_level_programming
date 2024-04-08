#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(argv[2])}`);
}
