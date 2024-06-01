#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (err, response, body) => {
  if (response) {
    let characterCount = 0;
    const films = JSON.parse(body);
    films.results.forEach(result => {
      result.characters.forEach(character => {
        if (character.includes('18')) {
          characterCount++;
        }
      });
    });
    console.log(characterCount);
  } else {
    console.error(err);
  }
});
