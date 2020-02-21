
console.log("I am working")

$("body").on("click", ".lol", function() {
  let cardID = $(this).parent().parent().parent().attr('id');

  console.log('clickeds',  '#' + cardID)
  let cardy = '#' + cardID

   $(cardy).prepend(
  `<div class="alert alert-Danger" role="alert">
  <h4 class="alert-heading">Yummy!</h4>
  <div class="form-group">
  <label for="exampleFormControlSelect1">When Did You Eat This Food?</label>
  <select class="form-control" id="exampleFormControlSelect1">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    <option>5</option>
  </select>
  </div>
  <hr>
  <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</div>`)
})
