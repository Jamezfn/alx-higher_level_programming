#!/usr/bin/node

const firstArg = process.argv[2];

if (isNaN(parseInt(firstArg)))
{
	console.log(“Missing number of occurrences”);
}
else
{
	const numOccurrences = parseInt(firstArg);
	for (let i = 0, i < numOccurrences, i++)
	{
		console.log(“C is fun”);
	}
}
