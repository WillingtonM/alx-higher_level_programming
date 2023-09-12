#!/usr/bin/node

/**
 * class Square that defines square and inherits from Rectangle
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

module.exports = Square;
