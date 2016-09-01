$(document).ready(function() {         

	var images=new Array(); // regular array (add an optional integer
	images[0]="/static/img/bg/0.jpg";
	images[1]="/static/img/bg/1.jpg";
	images[2]="/static/img/bg/2.jpg";
	images[3]="/static/img/bg/3.jpg";
	images[4]="/static/img/bg/4.jpg";

	Array.prototype.shuffle = function() {
		var len = this.length;
		var i = len;
		while (i--) {
			var p = parseInt(Math.random()*len);
			var t = this[i];
			this[i] = this[p];
			this[p] = t;
		}
	};

	images.shuffle();


	$.backstretch(images, {duration: 10000, fade: 1000});
	$('.backstretch').css({"opacity":"0.8"})

});