#!/usr/bin/node

const args = process.argv.slice(2);

const x = parseInt(args);

if (isNaN(x)) { console.log('Missing size'); } else if (x < 0) { // if x is negative
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
