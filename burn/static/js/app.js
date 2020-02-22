
console.log("I am working")

// $("body").on("click", ".macros", function() {
//   console.log("working")
//   let mac = $(this).parent().find(".macrosDiv")
//   console.log(mac)
// })

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


  $('body').on('click', '.logFood', function(event){
    console.log("this works")
    console.log(element.attr('data-id'))
    event.preventDefault();
    var element = $(this);
    $.ajax({
      url: 'search/add_food/',
      method: 'POST',
      data: {food_id: element.attr('data-id')},
      success: function(response){
        console.log(data)
      }
    });
  });
})

// reset
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
