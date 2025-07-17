$(function () {
	$('#toggle_header').on('click', function () {
		const $hdr = $('header');
		if ($hdr.hasClass('red')) {
			$hdr.removeClass('red').addClass('green')
		} else {
			$hdr.removeClass('green').addClass('red')
		}
	});
});
