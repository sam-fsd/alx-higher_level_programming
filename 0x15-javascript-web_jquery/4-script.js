const header = $('header');
$('#toggle_header').on('click', function () {
  ToggleClass();
});

function ToggleClass () {
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  } else {
    header.addClass('red');
  }
}
