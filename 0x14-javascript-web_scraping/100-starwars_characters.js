#!/usr/bin/node
// Script that prints all characters of Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, (err, resp, body) => {
  if (!err) {
    const chars = JSON.parse(body).characters;
    chars.forEach((character) => {
      request(character, function (err, resp, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
