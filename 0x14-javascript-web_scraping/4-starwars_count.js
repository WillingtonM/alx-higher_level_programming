#!/usr/bin/node
// Script that prints number of movies where character Wedge Antilles is present

const request = require('request');
const url = process.argv[2];
const char_id = '18';
let count = 0;

request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(char_id)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
