#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  console.log(Number(a) + Number(b));
}

add(argv[2], argv[3]);
