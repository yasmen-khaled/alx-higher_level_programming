#!/usr/bin/node
/*
script that computes the number of tasks completed by user id.
*/
const request = require('request');
const uri = process.argv[2];

request.get(uri, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = {};

    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.userId in result) {
          result[task.userId]++;
        } else {
          result[task.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
