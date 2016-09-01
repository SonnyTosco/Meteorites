$(document).ready(function() {
	$('.btn').click(function() {
				console.log('/events/'+$(this).attr('id'))

		$.post('/events/'+$(this).attr('id'), function(res) {
			$(this).toggleClass("join going");
			$(this).text($(this).text() == 'Join' ? 'Going!' : 'Join');
		});

	});
});