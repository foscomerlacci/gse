/**
 * Created by utente on 18/05/18.
 */

//
//
// (function($) {
//     $(function request_access($this){
//     console.log("button clicked");
//     var request_data = $this.id;
//     console.log("data: " + request_data);
//     $.ajax({
//         url: "crea_pdf_prestito/",
//         data : { request_data: request_data},
//         success : function(json) {
//             $("#request-access").hide();
//             console.log("requested access complete");
//         }
//     })
// });
// })(django.jQuery);



//
// (function($) {
//     $(document).ready(function () {                                        // ad ogni variazione della selectbox viene aggiornato la variabile
//         $('.submit-row.default').click(function () {
//             $(function crea_pdf_prestito($this){
//             console.log("button clicked");
//             var request_data = $this.id;
//             console.log("data: " + request_data);
//             $.ajax({
//             url: "crea_pdf_prestito/",
//             data : { request_data: request_data},
//             success : function(json) {
//             $("#request-access").hide();
//             console.log("requested access complete");
//         }
//     })
// });
//         });
//
//     });
// })(django.jQuery);


(function($) {
    $("#.submit-row.default").click(function(){
    alert("The paragraph was clicked.");
});
})(django.jQuery);

