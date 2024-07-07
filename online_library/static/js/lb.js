$(document).ready(function(){
$(".reviewform").submit(function(e){
  e.preventDefault();
  // console.log("s")
  $.ajax({
    data: $(this).serialize(),
    method: $(this).attr("method"),
    url: $(this).attr("action"),
    dataType: "json",
    success: function(response){
      // _html = '<p>'+ response.context.user +' -- '+ response.context.rating +'</p><p></p>'
      $(".reviewlist").prepend('<p>'+ response.context.user +' -- '+ response.context.rating +'</p><p></p>');
      $(".reviewform").hide()
    }
  })
})



    $(".filterform select").change(function(){

      $.ajax({
        data: $(".filterform").serialize(),
        method: $(".filterform").attr("method"),
        url: $(".filterform").attr("action"),
        dataType: "json",
        // beforeSend: function(){
        //   console.log($(".filterform").attr("action"))
        // },
        success: function(res){
          $(".list").html(res.data)
        },
        error: function(error){
          console.log(error)
        }
      })
    })
    $("select#id_faculty").change(function(){
      var faculty = $("select#id_faculty").val();
      $("select#id_department").val($("select#id_department").prop('defaultValue'));
      $("select#id_department option").show();
      $("div.store").each(function(index,department){
        $("select#id_department option").each(function(index,option){
        if ($(department).attr("testdata").toLowerCase().indexOf(faculty.toLowerCase())===-1){
          if ($(department).attr("testdata").toLowerCase().indexOf($(option).text().toLowerCase())!==-1){
              $(option).hide();
            }
          }
        });
      })
  })
  })
