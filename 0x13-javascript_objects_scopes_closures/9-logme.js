#!/usr/bin/node

let argumentCount = 0;
exports.logMe = function (item) {
	function print(){
		argumentCount++;
		console.log('${argumentCount - 1}: ${item}');
	}
	print();
};
