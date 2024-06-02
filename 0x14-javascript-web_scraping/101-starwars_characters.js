#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
const util = require('util');
const prequest = util.promisify(request);

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

(async function () {
  const characters = (await prequest(url, { json: true })).body.characters;
  for (const charUrl of characters) {
    const character = (await prequest(charUrl, { json: true })).body;
    console.log(character.name);
  }
})();
