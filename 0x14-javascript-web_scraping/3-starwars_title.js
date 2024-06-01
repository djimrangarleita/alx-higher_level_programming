#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, (err, response, body) => {
  if (response) {
    console.log(JSON.parse(body).title);
  } else {
    console.error(err);
  }
});
