#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const actorUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let filmsIn = 0;

request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === actorUrl) filmsIn++;
      }
    }
  }
  console.log(filmsIn);
});
