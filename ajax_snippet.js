
<script>
    function add_to_cart(prod_id) {
    let crs = document.getElementsByName('csrfmiddlewaretoken')
      console.log(crs);
      my_data = {
        prod_id:prod_id,
        csrfmiddlewaretoken:crs,
      }
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
