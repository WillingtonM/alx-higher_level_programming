#!/usr/bin/node
// Script that reads & prints content of file_name

const file_name = process.argv[2];
const fs = require('fs');

fs.readFile(file_name, 'utf8', function (error, content) {
  console.log(error || content);
});
