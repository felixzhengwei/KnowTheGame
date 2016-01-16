// $( document ).ready(function() {
//     $(".intro").fadeIn(2000);
//     setTimeout(function(){ $(".overlay").fadeOut(1000); }, 3000);
//     $( "#end-date" ).datepicker();
//       $.ajax({
//             url: '/tickers',
//             type: 'GET',
//             success: function(response) {
//                 console.log(response);
//                 responses = JSON.parse(response);
//                 $( "#index-value" ).autocomplete({
// 			      source: responses
// 			    });
//             },
//             error: function(error) {
//                 console.log(error);
//             }
//         });

//  	var indexArray = [];

//     $('#submit-button').click(function(event){
//         // Stop the form from actually submitting.        
//         event.preventDefault();            
        
//         // Capture the entered name and put it into the placeholder.
//         var oldEndDate = $('#end-date').val();
//         var endPrice = $('#end-price').val();
//         var dateArray = oldEndDate.split("/");
//         var endDate = dateArray[2] + "-" + dateArray[0] + "-" + dateArray[1];
//         var ticker = $("#index-value").val();
//         var start = "2014-01-01";
//         var end = endDate;
//         window.location.href = "/submit?ticker=" + ticker + "&start=" + start + "&end=" + end + "&endPrice=" + endPrice;

       
       
      
//     });

    
 
// });