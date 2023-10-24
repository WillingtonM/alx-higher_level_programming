#!/usr/bin/node
// Script that prints all characters of  Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let chars = [];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  chars = data.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === chars.length) {
    return;
  }

  request(chars[index], (err, resp, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
