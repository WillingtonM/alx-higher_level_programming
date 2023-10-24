#!/usr/bin/node
// Script that prints all characters of Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + movieId, function (err, resp, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const char = data.characters;
  for (const c of char) {
    request.get(c, function (err, resp, body1) {
      if (err) {
        console.log(err);
      }
      const dataAlt = JSON.parse(body1);
      console.log(dataAlt.name);
    });
  }
});
