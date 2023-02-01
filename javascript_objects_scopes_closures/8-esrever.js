#!/usr/bin/node
exports.esrever = function (list = []) {
<<<<<<< HEAD
  const newList = [];
  for (let i = list.length; i >= 0; i--) {
    newList.push(list[i]);
  }
  newList.shift();
  return newList;
};
=======
    const newList = [];
    for (let i = list.length; i >= 0; i--) {
      newList.push(list[i]);
    }
    newList.shift();
    return newList;
  };
>>>>>>> a48422103c23c7425dcf308552028e7d7bf3b8c2
