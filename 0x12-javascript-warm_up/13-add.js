#!/usr/bin/node

function add(a, b)
{
	if (isNaN(parseInt(a)) || isNaN(parseInt(b)))
	{
		return ("NaN");
	}
	return (parseInt(a) + parseInt(b));
}
module.exports = { add };
