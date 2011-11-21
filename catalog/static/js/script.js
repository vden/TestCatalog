$(function() {
      $("form.search")
          .submit(function() {
                      var term = $("input", "form.search").val();
                      if ($.trim(term) == "") 
                          return false;
                      else
                          return true;
                  });
  });