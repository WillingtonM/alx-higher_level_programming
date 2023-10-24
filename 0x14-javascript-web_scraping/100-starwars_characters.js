#!/usr/bin/node
// Script that prints all characters of Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const jsData = JSON.parse(body);
  const chars = jsData.characters;
  for (const character of chars) {
    request(character, (err, resp, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
