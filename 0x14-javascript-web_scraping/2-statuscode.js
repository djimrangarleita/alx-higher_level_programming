#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

const url = argv[2];

request(url, (err, response, body) => {
  if (response) {
    console.log('code:', response.statusCode);
  } else {
    console.error(err);
  }
});
