#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = 'X'.repeat(this.width);

    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

module.exports = Rectangle;
