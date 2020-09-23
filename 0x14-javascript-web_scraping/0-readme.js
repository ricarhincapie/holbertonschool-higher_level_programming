#!/usr/bin/node
const myArg = process.argv[2];
const fs = require('fs');
fs.readFile(myArg, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}
);
