#!/usr/bin/env node
const request = require('request')
url = 'https://jsonplaceholder.typicode.com/todos'
request.get(url, (error, response, body) => {
	if (error) {
		console.error(error)
	} else if (response.statusCode === 200) {
		const completed = {}
		const tasks = JSON.parse(body)
		for (const task of tasks) {
			if (task.completed === true) {
				if (completed[task.userId] === undefined) {
					completed[task.userId] = 1;
				} else {
					completed[task.userId]++;
				}
			}
		}
		console.log(completed);
	} else {
		console.log('An error occured. Status code: ' + response.statusCode);
	}
});
