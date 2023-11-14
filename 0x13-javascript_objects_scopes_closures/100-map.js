#!/usr/bin/node

const mylist = require('./100-data').list;

const mymap = new Map();
const myarray = [];

mylist.forEach((element, index) => {
  mymap.set(element, index);
});

for (const [key, value] of mymap.entries()) {
  myarray.push(key * value);
}

console.log(mylist);
console.log(myarray);
