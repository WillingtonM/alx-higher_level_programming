#!/usr/bin/node
// Script that reads & prints content of file_name

const file_name = process.argv[2];
const file_s = require('fs');

file_s.readFile(file_name, 'utf8', function (err, content) {
  console.log(err || content);
});
