#!/usr/bin/node
const myFile = process.argv[2];
const myString = process.argv[3];
const fs = require('fs');

fs.writeFile(myFile, myString, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
