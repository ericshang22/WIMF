
$(document).ready(function() {
    $("#spinner").hide();
    $("#search-button").click(function() {
        console.log("clicked");
        if (Boolean($("#meats").val()) || Boolean($("#vegetables").val())) {
        this.disabled = true;
        const url = "http://127.0.0.1:5000/search";
        const postInfo = { 
            meats : $("#meats").val().split(","),
            vegetables : $("#vegetables").val().split(",")
        }  
        $("#spinner").show();
        $.ajax({
			url: url,
			data: JSON.stringify(postInfo),
            type: 'POST',
            dataType: "json",
            contentType: "application/json;charset=UTF-8",
			success: function(response){
                console.log(response);
                window.location.href = response.redirect_link;
			},
			error: function(error){
                console.log(error);
			}
        });
         }
         else {
             alert("Please enter some ingredients");
         }

    });
});