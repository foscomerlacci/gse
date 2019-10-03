/**
 * Created by utente on 20/04/18.
 */

(function($) {
// inspect html to check id of category select dropdown.
            $(document).on('change', "select#id_produttore", function(){
                $.getJSON("/get_Prestiti_Modello/",{id_produttore: $(this).val(), id_tipo_dispositivo: $("select#id_tipo_dispositivo").val()}, function(j){
                     var options = '<option value="">---------</option>';

                     for (var i = 0; i < j.length; i++) {
                         options += '<option value="' + j[i][0] + '">' + j[i][1] + '</option>';
                     }
// {#                     alert(options);#}
// inspect html to check id of subcategory select dropdown.
                     $("select#id_modello").html(options);
                     $("input#id_seriale").val("");
                 });
             });

})(django.jQuery);
