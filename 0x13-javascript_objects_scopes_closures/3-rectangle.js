#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || w < 1 || h === undefined || h < 1) {
      return this;
    } else {
      this.width = w;
      this.height = h;
      this.print = function () {
        let tmp = '';
        for (let i = 0; i < h; i++) {
          for (let j = 0; j < w; j++) {
            tmp = tmp + 'X';
          }
          console.log(tmp);
          tmp = '';
        }
      };
    }
  }
};
