#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};
for (const [key, value] of Object.entries(dict)) {
	if (!newDict[value]) {
		newDict[value] = [];
	}
	newDict[value].push(String(key));
}
console.log(newDict);
