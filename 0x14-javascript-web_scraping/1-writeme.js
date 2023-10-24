#!/usr/bin/node
// Script that writes string to file

const fs = require('fs');
const url1 = process.argv[2];
const url2 = process.argv[3];

fs.writeFile(url1, url2, err => {
  if (err) console.log(err);
});
