#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request.get(url + id, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
