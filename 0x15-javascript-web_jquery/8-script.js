$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      for (const movie of data.results) {
        $('#list_movies').append($('<li></li>').text(movie.title));
      }
    }
  }
  );
});
