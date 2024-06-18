#!/usr/bin/node

exports.converter = function (base){
	function convert (number) {
		const digits = "0123456789ABCDEF"
		let result = "";

		if (number < 0){
			number = -number;
			result = "-"
		}

		while (number > 0){
			const remainder = number % base;
			result = digits[remainder] + results;
			number = math.floor(number / base);
		}

		return results;
	}
	return convert;
};
