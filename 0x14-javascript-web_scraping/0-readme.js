#!/usr/bin/node
/*
script that reads and prints the content of a file.
*/
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, file) {
  if (err) {
    return console.log(err);
  } else {
    console.log(file);
  }
});
