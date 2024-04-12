#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number(w) && Number(h)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
