#!/usr/bin/node
const myUrl = process.argv[2];
const request = require('request');

request.get(myUrl).on('response', function (response) {
  console.log('code: ' + response.statusCode);
}
);
