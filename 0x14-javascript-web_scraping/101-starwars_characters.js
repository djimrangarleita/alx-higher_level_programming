#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, (err, response, body) => {
  if (response) {
    const movie = JSON.parse(body);
    movie.characters.forEach(character => {
      request(character, (err, charResponse, charBody) => {
        if (response) {
          console.log(JSON.parse(charBody).name);
        } else {
          console.error(err);
        }
      });
    });
  } else {
    console.error(err);
  }
});
