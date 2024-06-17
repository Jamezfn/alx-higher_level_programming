#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length == 0)
{
	console.log(0);
}
else if
{
	const numbers = args.map(arg =>parseInt(arg));

	let Largest = -Infinity;
	let secondLargest = -Infinity;

	for (const num of numbers)
	{
		if (num > Largest)
		{
			secondLargest = Largest;
			Largest = num;
		}
		else if (num > secondLargest && num !== Largest)
		{
			secondLargest = num;
		}
	}

	console.log(secondLargest == -Infinity ? 0: secondLargest);
}
