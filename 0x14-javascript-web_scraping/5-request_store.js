#!/usr/bin/node
// script that gets contents of webpage & stores it in file

const file_s = require('fs');
const request = require('request');
request(process.argv[2]).pipe(file_s.createWriteStream(process.argv[3]));

