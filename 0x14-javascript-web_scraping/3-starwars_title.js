#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request({ url, json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    console.log(body.title);
  }
});
