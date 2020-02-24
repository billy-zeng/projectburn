console.log("I am working")

console.log($('#editProfile'))
console.log($('#resetButton'))

$("body").on("click", ".lol", function() {
  let cardID = $(this).parent().parent().parent().attr('id');


  // ID's with Spaces wouldn't work so this is a fix
  newID = cardID.split(' ').join('')

  $(this).parent().parent().parent().attr('id', newID)

  console.log('clickeds',  '#' + newID)
  let cardy = '#' + newID

   $(cardy).append(
  `<div class="alert alert-transparent" role="alert">
  <h4 class="alert-heading">Yummy!</h4>
  <form action="{% url 'search/add_food/' %}" method="POST" class="time-form">
  <div class="form-group">
  <label for="exampleFormControlSelect1">When Did You Eat This Food?</label>
  <select class="form-control" id="exampleFormControlSelect1">
    <option>Breakfast</option>
    <option>Lunch</option>
    <option>Dinner</option>
    <option>Snack</option>
  </select>
  <div class="row mt-2">
    <div class="col">
      <input type="text" class="form-control" placeholder="Enter Date">
    </div>
    <div class="col">
      <input type="text" class="form-control" placeholder="Enter Time">
    </div>
  </div>
  </div>
  <hr>
  <button type="submit" class="logFood btn btn-outline-dark btn-transparent btn-block">Log This Food!</button>
  </div>
  </form>`)


  // $('body').on('click', '.logFood', function(event){
  //   console.log("this works")
  //   // console.log(element.attr('data-id'))
  //   event.preventDefault();
  //   var element = $(this);
  //   $.ajax({
  //     url: '/add_food/',
  //     method: 'POST',
  //     // data: {food_id: element.attr('data-id')},
  //     success: function(response){
  //       console.log('success')
  //     }
  //   });
  // });
})

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

// $('body').on('submit', '#addFoodForm', function(event){
//   console.log("this works")
//   event.preventDefault();
//   const element = $(this);
//   const food_data_values = element.parent().parent().parent().find('#foodDataValues').val()
//   const food_name = element.parent().parent().parent().find('#foodName').val()
//   const food_calories = element.parent().parent().parent().find('#foodCalories').val()
//   const food_carbs = element.parent().parent().parent().find('#foodCarbs').val()
//   const food_fats = element.parent().parent().parent().find('#foodFat').val()
//   const food_proteins = element.parent().parent().parent().find('#foodProtein').val()
//   // const food_data_values = $('#foodDataValues').val()
//   const csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
//   $.ajax({
//     url: '/search/',
//     method: 'POST',
//     data: {
//       food_data: food_data_values,
//       food_name: food_name,
//       food_calories: food_calories,
//       food_carbs: food_carbs,
//       food_fats: food_fats,
//       food_proteins: food_proteins,
//       'csrfmiddlewaretoken': csrf_token
//     },
//     success: function(response){
//       console.log(response)
//     }
//   });
// });
