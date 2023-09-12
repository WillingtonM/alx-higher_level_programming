#!/usr/bin/node

// Script concatenates file passd as arguments into output file.
const args = process.argv.slice(2);
const fs = require('fs');
const data_first = fs.readFileSync('./' + args[0], 'utf-8');
const data_second = fs.readFileSync('./' + args[1], 'utf-8');
fs.writeFileSync('./' + args[2], data_first + data_second, 'utf-8');
