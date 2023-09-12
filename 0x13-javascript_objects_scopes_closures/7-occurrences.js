#!/usr/bin/node

// function returns the number of occurrences in list
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((cnt, currnt) => currnt === searchElement ? cnt + 1 : cnt, 0);
};

