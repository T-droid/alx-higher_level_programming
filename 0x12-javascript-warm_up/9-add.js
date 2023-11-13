#!/usr/bin/node

const args = process.argv.slice(2);
const first = parseInt(args[0]);
const second = parseInt(args[1]);

function add (a, b) {
  return (a + b);
}

console.log(add(first, second));
