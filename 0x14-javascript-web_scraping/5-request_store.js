#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const myUrl = process.argv[2];
const myFile = process.argv[3];

request.get(myUrl, function (err, response, body) { /* Aparently it needs all args */
  if (err) {
    console.error(err);
  } else {
    console.log(body);
    fs.writeFile(myFile, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
}
);
