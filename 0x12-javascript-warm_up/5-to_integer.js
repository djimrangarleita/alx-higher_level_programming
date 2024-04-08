#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log(Number(argv[2]));
}
