#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
<<<<<<< HEAD
  }
};
=======
  };
>>>>>>> a48422103c23c7425dcf308552028e7d7bf3b8c2
