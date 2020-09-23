#!/usr/bin/node
const request = require('request');
const myUrl = process.argv[2];
let count = 0;
const myObj = {};

request.get(myUrl, function (err, response, body) { /* Aparently it needs all args */
  if (err) {
    console.error(err);
  } else {
    const jsonResponse = JSON.parse(body);
    while (count < jsonResponse.length) {
      if (jsonResponse[count].completed === true) {
        if (jsonResponse[count].userId in myObj) {
          myObj[jsonResponse[count].userId] += 1;
        } else {
          myObj[jsonResponse[count].userId] = 1;
        }
      }
      count++;
    }
  }
  console.log(myObj);
});
