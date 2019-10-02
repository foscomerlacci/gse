// funzionanante
// (function($) {
//
// $(document).on($("div.submit-row.input").click, 'input',function() {
//
//         $("div.submit-row").hide();
//         {
//
//             notif({
//               msg: "<b>salvataggio corretto</b>",
//               type: "success"
//             });
//
//         }
//     });
//
// })(django.jQuery);

(function($) {

$(document).ready(function() {
        // $("div.submit-row.input.default").click(function() {
        $('input[name="_continue"]').click(function() {


            $("div.submit-row").hide();

                // notif({
                //     msg: "<b>salvataggio corretto</b>",
                //     type: "success"
                // });

        });

});

})(django.jQuery);



// (function($) {
//
// $(document).on('click', 'input.default',function(e) {
//         if(e.handled !== true) // This will prevent event triggering more then once
//         {
// 	    $.alert('Message here', {
// 	        // Enable auto close
//             autoClose: true,
//
//             // Auto close delay time in ms (>1000)
//             closeTime: 5000,
//
//         })
// 	    event.handled = true;
//         }
//     });
//
// })(django.jQuery);




// (function($) {


//funzionante

// $(document).on('click', 'input.default',function(e) {
//         if(e.handled !== true) // This will prevent event triggering more then once
//         {
//             var al = window.open('', 'inserimento corretto');
//             window.setTimeout(function() {al.close()}, 5000);
//             // alert("inserimento corretto");
//             event.handled = true;
//         }
//     });

// })(django.jQuery);





// funzionante

// (function($) {

// $(document).on('click', 'input.default',function(e){
// 	if(e.handled !== true) // This will prevent event triggering more then once
//     var w = window.open('','','width=100,height=100')
// 	w.document.write('inserimento corretto')
// 	w.focus()
// 	setTimeout(function() {w.close();}, 2000)
// 	event.handled = true;
//  	});

// })(django.jQuery);


// (function($) {
//
// $(document).on('click', 'input.default',function(e){
// 	if(e.handled !== true) // This will prevent event triggering more then once
// 	    $.alert({
//         title: 'Alert!',
//         content: 'Simple alert!',
//     });
//  	});
//
// })(django.jQuery);






    //
    // $.alert({
    //     title: 'Alert!',
    //     content: 'Simple alert!',
    // });









// function tempAlert(msg,duration)
// {
//  var el = document.createElement("div");
//  el.setAttribute("style","position:absolute;top:40%;left:20%;background-color:white;");
//  el.innerHTML = msg;
//  setTimeout(function(){
//   el.parentNode.removeChild(el);
//  },duration);
//  document.body.appendChild(el);
// }







// $(document).ready(function() {
//     $("#testDiv").dialog({
//         height: 140,
//         modal: true,
//         open: function(event, ui){
//            setTimeout("$('#testDiv').dialog('close')",5000);
//         }
//     });
//  });