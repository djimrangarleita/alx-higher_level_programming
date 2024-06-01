#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

const url = argv[2];

request(url, (err, response, body) => {
  const usersList = {};
  if (response) {
    const result = JSON.parse(body);
    result.forEach(user => {
      if (user.completed) {
        const cUserId = String(user.userId);
        if (!(cUserId in usersList)) {
          usersList[cUserId] = 0;
        }
        usersList[cUserId]++;
      }
    });
    console.log(usersList);
  } else {
    console.error(err);
  }
});
