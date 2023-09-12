#!/usr/bin/node
/**
 * Check parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0) || !h || !w) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
