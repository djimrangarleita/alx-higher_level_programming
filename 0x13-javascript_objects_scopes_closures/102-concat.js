#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

const path1 = argv[2];
const path2 = argv[3];
const output = argv[4];

fs.readFile(path1, 'utf8', (error, content) => {
  if (error) {
    console.error('An error occured while reading file 1');
    return;
  }

  fs.readFile(path2, 'utf8', (error, content2) => {
    if (error) {
      console.error('An error occured while reading file 2');
      return;
    }

    const fContents = content + content2;

    fs.writeFile(output, fContents, 'utf8', err => {
      if (err) {
        console.error('An error occured while writing file');
      }
    });
  });
});
