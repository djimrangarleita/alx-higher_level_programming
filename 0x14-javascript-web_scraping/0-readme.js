#!/usr/bin/node
const fs = require('node:fs');
const { argv } = require('node:process');

const path = argv[2];

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
