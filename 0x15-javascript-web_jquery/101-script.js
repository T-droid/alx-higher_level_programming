$(document).ready(() => {
  $('#add_item').click(() => {
    $('.my_list').append('<li>item</li>');
  });
  $('#remove_item').click(() => {
    $('.my_list li:last').remove();
  });
  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});
