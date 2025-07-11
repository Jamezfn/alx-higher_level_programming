#!/usr/bin/env node

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const request = require("request");

request.get(url, (error, response, body) => {
        if (error) {
                console.error(error);
        } else if (response.statusCode === 200) {
                const actorsUrl = JSON.parse(body).characters;
                for (const urls of actorsUrl) {
                        request.get(urls, (error, response, body) => {
                                if (!error) {
                                        const actor = JSON.parse(body).name;
                                        console.log(actor);
                                }
                        });
                }
        } else {
                console.log('Not found');
        }
});
