#!/usr/bin/env node

const url = process.argv[2]
const request = require("request")

request.get(url, (error, response, body) => {
        if (error) {
                console.error(error);
        } else if (response.statusCode === 200) {
                const films = JSON.parse(body).results;
                console.log(films.reduce((count, movie) => {
                        return movie.characters.find((character) => character.endsWith('/18/'))
                        ? count + 1
                        : count;
                }, 0))
        }
})
