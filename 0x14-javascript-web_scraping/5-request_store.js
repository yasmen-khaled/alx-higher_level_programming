#!/usr/bin/node
/*
script that gets the contents of a webpage and stores it in a file.
*/

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
