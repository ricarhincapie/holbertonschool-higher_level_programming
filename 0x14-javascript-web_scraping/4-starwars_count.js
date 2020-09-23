#!/usr/bin/node
const request = require('request');
const myUrl = process.argv[2];
const myChar = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;

request.get(myUrl, function (err, response, body) { /* Aparently it needs all args */
  if (err) {
    console.error(err);
  } else {
    const jsonResponse = JSON.parse(body).results; /* Converts to JS object */
    /* console.log(jsonResponse.length) */
    /* console.log(JSON.stringify(jsonResponse)); */
    for (let i = 0; i < jsonResponse.length; i++) {
      if (jsonResponse[i].characters.includes(myChar)) { /* Includes method */
        count++;
      }
    }
    console.log(count);
  }
}
);
