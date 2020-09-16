#!/usr/bin/node

let first = process.argv[2];

first = parseInt(first);

if (isNaN(first)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < first; i++) {
    console.log('C is fun');
  }
}
