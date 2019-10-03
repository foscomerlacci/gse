/**
 * Created by utente on 03/10/19.
 */

(function($) {

$(document).ready(function() {


            if ($("li.success").is(":visible")) {
                    $("li.success").hide();

                    notif({
                    msg: "<b>salvataggio corretto</b>",
                    position: "center",
                    timeout: 3000,
                    fade: true,
                    // opacity: 0.8,
                    type: "success"});


            }else if($("p.errornote").is(":visible")) {
                    $("p.errornote").hide();

                    notif({
                    msg: "<b>si è verificato un errore</b>",
                    position: "center",
                    timeout: 3000,
                    fade: true,
                    // opacity: 0.8,
                    type: "error"});


            }

});

})(django.jQuery);