#!/usr/bin/node

class Rectangle {
	constructor (w, h){
		if (Number.isInteger(w) && w > 0 && Number.isinteger(h) && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			this.width = undefined;
			this.height = undefined;
		}
	}

	print() {
		for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width));}
	}
}

module.exports = Rectangle;