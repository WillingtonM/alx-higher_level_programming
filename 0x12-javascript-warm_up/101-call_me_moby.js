#!/usr/bin/node

exports.callMeMoby = function (x, callback) {
  for (let j = 0; j < x; j++) {
    callback(x);
  }
};
