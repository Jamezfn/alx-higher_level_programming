#!/usr/bin/node
const arg = process.argv.slice(2).map(num => parseInt(num));
if (arg.length <= 1) {
	console.log(0);
} else {
	const sorted = arg.sort((a, b) => (b - a));
	console.log(sorted[1]);
}
