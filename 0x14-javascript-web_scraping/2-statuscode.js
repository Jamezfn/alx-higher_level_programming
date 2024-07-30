#!/usr/bin/node
const request = require('request')
request.get(process.argv[2]).on('request', function (response) {
  console.log('code: ${reponse.statusCode}');
});
