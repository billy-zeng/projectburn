console.log('js up')

// reset foods
$('.reset').on('click', function(event){
  console.log('click')
  event.preventDefault();
  $.ajax({
    url: '/clear_foods/',
    method: 'GET',
    success: function(response){
      console.log(response)
      // clear cards on the page
    }
  });
});