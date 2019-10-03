/**
 * Created by utente on 10/04/18.
 */
(function($) {
    $(document).ready(function () {                                        // ad ogni variazione della selectbox viene aggiornato la variabile
        $('#id_tipo_dispositivo').on('change', function () {
            var tipo = $('#id_tipo_dispositivo :selected').val();
            // alert(tipo);
            $.ajax({
                type:"POST",
                URL:'gse/dispositivi/forms.py',
                // URL : '{% url "myapp:toolbox.py" %}',
                data : {
                    'tipo' : tipo,

                },

        });
            // alert(tipo)
        });

    });
})(django.jQuery);