/**
 * Created by utente on 19/07/18.
 */

(function($) {
// inspect html to check id of category select dropdown.
            $(document).on('focusin', "select#id_fk_beneficiario", function(){


                     $("select#id_asset").html('<option value="">---------</option>');

             });

})(django.jQuery);
