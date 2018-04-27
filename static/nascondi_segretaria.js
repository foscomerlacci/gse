(function($) {
    $(function() {
        var selectField = $('#id_ruolo'),
            verified = $('.form-row.field-segretaria_associata');

        function toggleVerified(value) {
             if (value === 'seg') {
                verified.hide();
             } else {
                 verified.show();
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

