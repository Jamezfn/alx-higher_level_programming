#!/usr/bin/node

const firstArg =process.argv[2];
const secondArg =process.argv[3];

function add(a, b)
{
	if (isNaN(parseInt(a)) || isNaN(parseInt(b)))
	{
		return ("NaN")
	}
	return (parseInt(a) + parseInt(b));
}

if (isnaN(parseInt(firstarg)) || isNaN(parseInt(secondArg)))
{
	console.log("NaN");
}
else
{
	const sum = add(firstArg, secondArg);
	console.log(sum);
}
