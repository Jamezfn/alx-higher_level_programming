#!/usr/bin/node

class Rectangle {
	constructor(w, h){
		if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0){
			this.width;
			this.height;
		} else {
			this.width = undefined;
			this.height = undefined;
		}
	}
}
