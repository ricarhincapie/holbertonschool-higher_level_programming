#!/usr/bin/node
const request = require('request');
const myId = process.argv[2];

const myUrl = 'https://swapi-api.hbtn.io/api/films/' + myId;

request.get(myUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
}
);
