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
}

module.exports = Rectangle;
