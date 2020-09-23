#!/usr/bin/node
const request = require('request');
const myUrl = process.argv[2];
const myChar = '18';
let count = 0;

request.get(myUrl, function (err, response, body) { /* Aparently it needs all args */
  if (err) {
    console.error(err);
  } else {
    const jsonResponse = JSON.parse(body).results; /* Converts to JS object */
    /* console.log(jsonResponse.length) */
    /* console.log(JSON.stringify(jsonResponse)); */

    for (const film of jsonResponse) {
      for (const string of film.characters) {
        if (string.includes(myChar)) { /* Includes method */
          count++;
        }
      }
    }
    console.log(count);
  }
}
);
