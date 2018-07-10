/**
 * Created by utente on 09/07/18.
 */

// Al caricamento della pagina viene verificato lo stato della checkbox #id_disponibile e se non risulta "checked" si nasconde il div '.form-row.field-data_checkout' con effetto fadeOut


// (function($) {
//
// $(document).ready(function(){
//
//     var disponibile = $('#id_disponibile');
//
//         if($(disponibile).attr("checked")){
//             $('.form-row.field-data_checkout').fadeIn('slow');}
//         else{
//             $('.form-row.field-data_checkout').fadeOut('slow');}
//
//         });
//
//
// })(django.jQuery);



// Al caricamento della pagina viene verificato lo stato della checkbox #id_disponibile e se non risulta "checked" si nasconde il div '.form-row.field-data_checkout'

(function($) {

$(document).ready(function(){

    var disponibile = $('#id_disponibile');

        if($(disponibile).attr("checked")){
            $('.form-row.field-data_checkout').show();}
        else{
            $('.form-row.field-data_checkout').hide();}

        });


})(django.jQuery);
