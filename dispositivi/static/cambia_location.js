/**
 * Created by utente on 19/07/18.
 */

(function($) {
// inspect html to check id of category select dropdown.
            $(document).on('focusin', "select#id_location", function(){


                     $("input#id_palazzo").val("");
                     $("input#id_piano").val("");
                     $("input#id_stanza").val("");

             });

})(django.jQuery);
