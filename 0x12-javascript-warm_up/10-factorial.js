#!/usr/bin/node

const { argv } = require('node:process');

function factorial (myNum) {
  if (isNaN(myNum)) {
    console.log(1);
    return;
  }
  myNum = Number(myNum);
  let result = 1;
  for (let i = myNum; i > 0; i--) {
    result *= i;
  }
  console.log(result);
}

factorial(argv[2]);
