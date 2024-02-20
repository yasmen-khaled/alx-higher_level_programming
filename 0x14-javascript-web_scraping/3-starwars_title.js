#!/usr/bin/node

/*
 script that prints the title of a Star Wars movie where the episode number matches a given integer.
*/

const request = require('request');
const reqURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(reqURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
