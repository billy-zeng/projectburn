console.log('js up')

$('.reset').on('click', function(event){
  console.log('click')
  event.preventDefault();
  $.ajax({
    url: '/clear_foods/',
    method: 'GET',
    success: function(response){
      console.log(response)
    }
  });
});