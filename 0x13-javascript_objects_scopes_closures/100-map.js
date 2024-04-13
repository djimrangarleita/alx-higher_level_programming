#!/usr/bin/node

const list = require('./100-data.js').list;

const compList = list.map((elt, idx) => (elt * idx));

console.log(list);
console.log(compList);
