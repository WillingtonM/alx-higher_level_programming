#!/usr/bin/node
// Script that writes string to file

const file_s = require('fs');
file_s.writeFile(process.argv[2], process.argv[3], err => {
  if (err) console.log(err);
});
