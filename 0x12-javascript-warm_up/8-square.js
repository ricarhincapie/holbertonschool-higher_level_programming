#!/usr/bin/node

let first = process.argv[2];
let tmp = '';
first = parseInt(first);

if (isNaN(first)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < first; i++) {
    for (let j = 0; j < first; j++) {
      tmp = tmp + 'X';
    }
    console.log(tmp);
    tmp = '';
  }
}
