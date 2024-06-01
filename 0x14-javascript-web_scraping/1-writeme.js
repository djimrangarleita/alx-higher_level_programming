#!/usr/bin/node
const fs = require('node:fs');
const { argv } = require('node:process');

const path = argv[2];
const content = argv[3];

fs.writeFile(path, content, err => {
  if (err) {
    console.log(err);
  }
});
