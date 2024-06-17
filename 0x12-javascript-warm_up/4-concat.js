#!/usr/bin/node

const firstArg = process.agrv[2];
const secondArg = process.argv[3];

if (firstArg && secondArg)
{
	console.log('${firstArg} is ${secondAgv}');
}
else
{
	console.log("Not enough arguments. Please provibe two arguments.");
}
