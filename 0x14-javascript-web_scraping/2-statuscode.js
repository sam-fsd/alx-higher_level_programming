#!/usr/bin/node
// a script that display the status code of a GET request.
// The first argument is the URL to request (GET)

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  console.log('Code:', response.statusCode);
});
