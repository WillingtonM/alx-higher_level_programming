#!/usr/bin/node
const dict = require('./101-data.js').dict;

const n_dict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (n_dict[dict[occurences]] === undefined) {
    n_dict[dict[occurences]] = [occurences];
  } else {
    n_dict[dict[occurences]].push(occurences);
  }
});

console.log(n_dict);
