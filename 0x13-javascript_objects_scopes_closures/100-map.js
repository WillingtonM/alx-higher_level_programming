#!/usr/bin/node
// Maps array and multiplies each element eith it's index
const list = require('./100-data').list;
console.log(list);
console.log(list.map((num, elem) => num * elem));
