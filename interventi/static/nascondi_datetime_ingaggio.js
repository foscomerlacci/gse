(function($) {
    $(function() {
        var selectField = $('#id_tipo_ingaggio'),
            verified = $('.form-row.field-datetime_ingaggio');

        function toggleVerified(value) {
             if (value === 'telefonata utente') {
                verified.show();
             } else {
                 verified.hide();
                 id_datetime_ingaggio_0.value = ''
                 id_datetime_ingaggio_1.value = ''
             }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);

