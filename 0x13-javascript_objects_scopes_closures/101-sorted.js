#!/usr/bin/node

const dict = require('./101-data').dict;

const keys = Object.keys(dict).sort((a, b) => a - b);
const myObj = {};

keys.forEach(key => {
  if (!myObj[dict[key]]) {
    myObj[dict[key]] = [];
  }
  myObj[dict[key]].push(key);
});

console.log(myObj);
