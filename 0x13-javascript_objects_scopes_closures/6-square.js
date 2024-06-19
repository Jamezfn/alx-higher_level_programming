#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
	charPrint(char = 'X') {
		if (this.width && this.height){
			let output = "";
			for (let i = 0; i < this.width; i++){
				for (let j = 0; j < this.width; j++){
					output += char;
				}
				output += "\n";
			}
			console.log(output);
		}else {
			console.log("This is not a rectangle");
		}
	}
}
