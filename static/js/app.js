// Search Bar for Credit Entries
$(document).ready(function(){
  $("#creditsearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#creditsearch tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
// Search Bar for Debit Entries
$(document).ready(function(){
  $("#debitsearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#debitsearch tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
// Search Bar for Transfer Entries
$(document).ready(function(){
  $("#transfersearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#transfersearch tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});


// Credit Data Entry
document.getElementById("creditbtn").addEventListener("click", function() {
    let id_amt = document.getElementById('id_amt').value;
    let id_tag = document.getElementById('id_tag').value;
    let crs = document.getElementsByName('csrfmiddlewaretoken')[0].value
    my_data = {csrfmiddlewaretoken:crs,amt:id_amt, tag:id_tag};

    console.log(my_data)

    $.ajax({
      url: "/creditsave/",
      method: "POST",
      data: my_data,
      // dataType: "json",
      success: function (data){
        if (data.status == 'done'){
          // document.getElementById('creditform').reset()
                
          document.getElementsByTagName('form')[1].reset()        
        }
      }
    });
  });
      
// Debit Data Entry
document.getElementById("debitbtn").addEventListener("click", function() {
    let id_amt = document.getElementById('debit_amt').value;
    let id_tag = document.getElementById('debit_tag').value;
    let crs = document.getElementsByName('csrfmiddlewaretoken')[0].value
    my_data = {csrfmiddlewaretoken:crs,amt:id_amt, tag:id_tag};

    console.log(my_data)

    $.ajax({
      url: "/debitsave/",
      method: "POST",
      data: my_data,
      // dataType: "json",
      success: function (data){
        if (data.status == 'done'){
          document.getElementById('debitform').reset()
                
        }
      }
    });
  });
      
// Transfer Data Entry
document.getElementById("transferbtn").addEventListener("click", function() {
    let id_amt = document.getElementById('transfer_amt').value;
    let id_tag = document.getElementById('transfer_tag').value;
    let crs = document.getElementsByName('csrfmiddlewaretoken')[0].value
    my_data = {csrfmiddlewaretoken:crs,amt:id_amt, tag:id_tag};

    console.log(my_data)

    $.ajax({
      url: "/transfersave/",
      method: "POST",
      data: my_data,
      // dataType: "json",
      success: function (data){
        if (data.status == 'done'){
          document.getElementById('transferform').reset()
                
        }
      }
    });
});
      
// Credit / Debit /Transfer Fast-Button 
function myfun (id){
  my_data = {id:id}
  console.log(my_data)
  $.ajax({
    url: "/fastbtn/",
    method: "GET",
    data: my_data,
    // dataType: "json",
    success: function (data){
      if (data.status == 'done'){
              
      }
    }
  });
  
}
  
// Fast Button Generate
document.getElementById("fastbtngen").addEventListener("click", function() {
  let id_amt = document.getElementById('fast_amt').value;
  let fast_btn_type = document.getElementById('fast_btn_type').value;
  let crs = document.getElementsByName('csrfmiddlewaretoken')[0].value
  my_data = {csrfmiddlewaretoken:crs,amt:id_amt,btn_type:fast_btn_type};

  console.log(my_data)

  $.ajax({
    url: "/generatefastbtn/",
    method: "POST",
    data: my_data,
    // dataType: "json",
    success: function (data){
      if (data.status == 'done'){
        document.getElementById('genfastbtnform').reset()
              
      }
    }
  });

});


