#!/usr/bin/node

let count = 0;
module.exports.logMe = function (item) {
  function print () {
    console.log(`${count++}: ${item}`);
  }
  print();
};
