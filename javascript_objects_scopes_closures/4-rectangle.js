#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
<<<<<<< HEAD

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
=======
  
  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
  
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
  
    double () {
      [this.width, this.height] = [this.width * 2, this.height * 2];
    }
  };
>>>>>>> a48422103c23c7425dcf308552028e7d7bf3b8c2
