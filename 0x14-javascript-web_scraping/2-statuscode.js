#!/usr/bin/node
// Script that display status code of GET request

const req = require('request');
const url = process.argv[2];

req.get(url, (req, resp) => {
  if (req) {
    console.log(req);
  } else {
    console.log(`code: ${resp.statusCode}`);
  }
});
