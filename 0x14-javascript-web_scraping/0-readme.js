#!/usr/bin/node
// Script that reads & prints content of file_name

const file_name = process.argv[2];
const file_s = require('fs');

file_s.readfile_name(file_name, 'utf8', (err, dat) => {
  if (err) {
    console.log(err);
  } else {
    console.log(dat);
  }
});
