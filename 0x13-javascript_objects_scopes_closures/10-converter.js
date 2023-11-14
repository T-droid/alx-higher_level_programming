#!/usr/bin/node

module.exports.converter = function (base) {
  function myconverter (number) {
    return (number.toString(base));
  }
  return myconverter;
};
