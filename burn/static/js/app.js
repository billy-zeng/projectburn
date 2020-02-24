// reset
$('#resetButton').on('click', function(event){
  console.log('click')
  event.preventDefault();
  $.ajax({
    url: '/clear_foods/',
    method: 'GET',
    success: function(response){
      window.location = '/dashboard/';
    }
  });
}); 

// edit profile
$('#editProfile').on('click', function(event){
  console.log('click')
  event.preventDefault();
  $.ajax({
    url: '/edit_profile/',
    method: 'GET',
    success: function(response){
      window.location = '/edit_profile/';
    }
  });
}); 
