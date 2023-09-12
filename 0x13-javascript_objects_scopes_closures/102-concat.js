#!/usr/bin/node
const fs = require('fs');
const data_a = fs.readFileSync(process.argv[2], 'utf8');
const data_b = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], data_a + data_b);
