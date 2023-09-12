#!/usr/bin/node

exports.addMeMaybe = function (x, callback) {
  x = x + 1;
  callback(x);
};
