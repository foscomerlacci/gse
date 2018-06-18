/**
 * Created by utente on 07/06/18.
 */
(function($) {

    //al caricamento della pagina nascondo il div con all'interno la class assegnata a to_hide

    $(document).ready(function() {
        var
            to_hide = $('.form-row.field-tecnico_ritiro.field-fine_prestito');

        to_hide.hide();

    });
})(django.jQuery);