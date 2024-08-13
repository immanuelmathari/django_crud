// this comes from the id message timer in base.html for the message popup timer. the alert
var message_timeout = document.getElementById("message-timer");

setTimeout(function() 
{
    message_timeout.style.display = "none";
}, 3000);