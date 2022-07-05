
<script>
    function add_to_cart(prod_id) {
    let crs = document.getElementsByName('csrfmiddlewaretoken')[0].value
    // put your logics here      

      $.ajax({
      url: "/creditsave/",
      method: "POST",
      data: my_data,
      success: function (data){
        
      }
    });

    }
  </script>
