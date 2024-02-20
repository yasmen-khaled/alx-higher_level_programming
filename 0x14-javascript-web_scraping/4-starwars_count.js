#!/usr/bin/node
/*
script that prints the number of movies where the character “Wedge Antilles” is present.
*/

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let count = 0;
    for (const film of JSON.parse(body).results) {
      for (const chracter of film.characters) {
        if (chracter.search('/api/people/18/') > 0) { count++; }
      }
    }
    console.log(count);
  }
});
