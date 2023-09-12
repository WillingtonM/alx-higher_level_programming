#!/usr/bin/node
// Function converts number from Base10 to given base
exports.converter = function (base) {
  return function (b_number) {
    return b_number.toString(base);
  };
};
