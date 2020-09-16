#!/usr/bin/node

const first = process.argv[2];

if (first === undefined) {
  console.log('Not a number');
} else {
  const result = parseInt(first);
  if (isNaN(result)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + result);
  }
}
