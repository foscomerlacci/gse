/**
 * Created by utente on 10/04/18.
 */
(function($) {
    $(document).ready(function () {                                        // ad ogni variazione della selectbox viene aggiornato la variabile
        $('#id_produttore').on('change', function () {
            var produttore = $('#id_produttore :selected').val();
            // alert(produttore);
            // return produttore

        })

    });
})(django.jQuery);