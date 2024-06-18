#!/usr/bin/node

class Rectangle {
	constructor(w, h){
		if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			this.width = undefined;
			this.height = undefined;
		}
	}

	print(){
		if (this.width && this.height) {
			let output = "";
			for (let i = 0; i < this.width; i++) {
				for (let j = 0; i < this.width; j++) {
					output += "X";
				}
				output += "\n";
			}
			console.log(output);
		} else {
			console.log("This is not a rectangle");
		}
	}

	rotate() {
		if (this.width && this.height) {
			const temp = this.width;
			this.width = this.height;
			this.height = temp;
		}
	}

	double() {
		if (this.width && this.height){
			this.width *= 2;
			this.height *= 2;
		}
	}
}

class Square extends Rectangle{
	constructor(size);
	super(size, size);
}

module.exports = Square;
