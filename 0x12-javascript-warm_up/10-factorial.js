#!/usr/bin/node

const firstArg = process.argv[2];

function  factorial(n)
{
	if (n == 0)
	{
		return (1);
	}

	if (isNaN(n))
	{
		return (1);
	}

	return (n * factorial(n - 1));
}

if (isNaN(parseInt(firstArg)))
{
	console.log(1);
}
else
{
	const num = parseInt(firstArg);
	const result = factoriala(num);
	console.log(result);
}
