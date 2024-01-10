$.ajax({
  type: 'GET',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: (data) => {
    $('#hello').append('<p>' + data.hello + '</p>');
  }
});
