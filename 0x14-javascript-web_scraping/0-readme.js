#!/usr/bin/node
// Script that reads & prints content of fileName

const fileName = process.argv[2];
const fs = require('fs');

fs.readFile(fileName, 'utf8', function (err, content) {
  console.log(err || content);
});
