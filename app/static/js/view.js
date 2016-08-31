$(document).ready(function() {
	$.backstretch(["/static/img/background.jpg", 
		"https://upload.wikimedia.org/wikipedia/commons/6/6e/Veil_Nebula_-_NGC6960.jpg",
		"https://upload.wikimedia.org/wikipedia/commons/d/d6/Hs-2009-25-e-full_jpg.jpg"],
		{duration: 5000, fade: 2000});
	$('.backstretch').css({"opacity":"0.8"})

	$('.comments').hide();

	$('.messages').click(function() {
		$(this).parent().next().next().toggle();
	})	
});