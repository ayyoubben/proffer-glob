
$('#btn1').click(function(){
    $('#inputUsername').prop('disabled', false);
    $('#inputFirstName').prop('disabled', false);
    $('#inputEmail').prop('disabled', false);
    $('#inputAdresse').prop('disabled', false);
    $('#inputNum').prop('disabled', false);
});

function EnableInput(btn1) {
    var txtPassportNumber = document.getElementById("txtPassportNumber");
    if (btnPassport.value == "Yes") {
        txtPassportNumber.removeAttribute("disabled");
    } else {
        txtPassportNumber.setAttribute("disabled", "disabled");
    }
}