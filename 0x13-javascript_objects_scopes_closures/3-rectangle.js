#!/usr/bin/node

class Rectangle {
	constructor (w, h){
		if (Number>isInteger(w) && w > 0 && Number.isinteger(h) && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			this.width = undefined;
			this.height = undefined;
		}
	}

	print() {
		if (this.width && this.height) {
			let output = "";
			for (let i = 0; i < this.height; i++){
				for (let j = 0; j < this.width; j++){
					output += "X";
				}
				output += "\n";
			}
			console.log(output);
		}
	}
}

module.exports = Rectangle;
