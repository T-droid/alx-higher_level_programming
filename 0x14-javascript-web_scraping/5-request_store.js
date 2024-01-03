#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3]

request({url: url, json: false}, (error, response, body) => {
    if (error)
    {
        console.error(error);
    }
    else if (response.statusCode === 200)
    {
        fs.writeFile(file, body, 'utf-8', (error) => {
            if (error)
            {
                console.error(error);
            }
        });
    }
})
