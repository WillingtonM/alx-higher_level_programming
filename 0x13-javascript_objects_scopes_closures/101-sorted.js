#!/usr/bin/node
const data_dict = require('./101-data').dict;
console.log(Object.entries(data_dict).reduce(function (x, x_idx) {
  x[x_idx[1]] = (x[x_idx[1]] || []).concat(x_idx[0]);
  return x;
}, {}));