#!/usr/bin/node
// Script that prints title of Star Wars movie where episode num matches given int

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, resp, body) {
  console.log(err || JSON.parse(body).title);
});
