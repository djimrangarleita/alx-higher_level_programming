#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
const fs = require('node:fs');

const url = argv[2];
const path = argv[3];

request(url, (err, response, body) => {
  if (response) {
    fs.writeFile(path, body, err => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.error(err);
  }
});
