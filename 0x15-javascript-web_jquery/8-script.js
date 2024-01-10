$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (data) => {
    $.each(data.results, (i, value) => {
      $('#list_movies').append('<li>' + value.title + '</li>');
    });
  }
});
