$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const code = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: code })
      .done(function (data) {
        $('#hello').text(data.hello || 'Translation not found');
      })
      .fail(function () {
        $('#hello').text('Error fetching translation');
      });
  });
});

