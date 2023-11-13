#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

function fact (n) {
  if (n === 0 || n === 1 || isNaN(n)) { return (1); } else { return n * fact(n - 1); }
}

console.log(fact(num));
