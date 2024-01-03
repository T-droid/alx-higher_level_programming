#!/usr/bin/node

const request = require('request');
const util = require('util');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const asyncRequest = util.promisify(request);

async function fetchCharacterDetails (characterUrl) {
  const { body } = await asyncRequest({ url: characterUrl, json: true });
  console.log(body.name);
}

(async () => {
  try {
    const { body } = await asyncRequest({ url, json: true });
    const characters = body.characters;

    // Iterate through each character URL and fetch details
    for (const characterUrl of characters) {
      await fetchCharacterDetails(characterUrl);
    }
  } catch (error) {
    console.error(error);
  }
})();
