#!/usr/bin/node

/**
 * class Square that defines square and inherits from Square as SquareB
 */
const SquareB = require('./5-square');

class Square extends SquareB {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let z = 0; z < this.height; z++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};

module.exports = Square;
