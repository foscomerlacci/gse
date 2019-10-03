/**
 * Created by utente on 03/10/19.
 */

(function($) {

$(document).ready(function() {


            if ($("li.success").is(":visible")) {
                    $("li.success").hide();
                    notif({
                    msg: "<b>salvataggio corretto</b>",
                    type: "success"});

                    // $("li.success").hide();

            }else if($("p.errornote").is(":visible")) {
                    $("p.errornote").hide();
                    notif({
                    msg: "<b>si è verificato un'errore</b>",
                    type: "error"});


            }

});

})(django.jQuery);