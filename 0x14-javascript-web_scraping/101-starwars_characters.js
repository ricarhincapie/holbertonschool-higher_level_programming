#!/usr/bin/node
const request = require('request');
const myId = process.argv[2];

const myUrl = 'https://swapi-api.hbtn.io/api/films/' + myId;

request.get(myUrl, function (err, response, body) { /* Aparently it needs all args */
  if (err) {
    console.error(err);
  } else {
    const jsonResponse = JSON.parse(body);
    for (const charUrl of jsonResponse.characters) {
      request.get(charUrl, function (err, response, body) {
        if (err) {
          console.error(err);
        } else {
          const charResponse = JSON.parse(body);
          console.log(charResponse.name);
        }
      });
    }
  }
}
);
