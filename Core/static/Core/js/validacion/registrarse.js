$(document).ready(function () {

    $("#formRegi").submit(function (e) {
        var nick = $("#username1").val();
        var nombre = $("#nombre1").val();
        var ape = $("#apellido1").val();
        var mail = $("#email1")
        var pass1 = $("#contrasena1").val();
        var pass2 = $("#contrasena2").val();
      

        let mensajeMostrar = "";
        let entrar = true;

        
        if (!esMayuscula(nombre.charAt(0))) {
            mensajeMostrar += "<br>La primera letra del nombre debe ser mayúscula<br>";
            entrar = false;
        }

        if (nombre.length > 50) {
            mensajeMostrar += "El nombre puede contener un máximo de 50 caracteres<br>";
            entrar = false;
        }


        if (!ape == "") {

            if (!esMayuscula(ape.charAt(0))) {
                mensajeMostrar += "La primera letra del apellido debe ser mayúscula<br>";
                entrar = false;
            }
            if (ape.length > 50) {
                mensajeMostrar += "El apellido puede contener un máximo de 50 caracteres<br>";
                entrar = false;
            }
        }

        

        if (nick.length < 4 || nick.length > 60) {
            mensajeMostrar += "El nombre de usuario debe tener entre 4 y 60 caracteres<br>";
            entrar = false;
        }

        if (mail.length > 30) {
            mensajeMostrar += "El correo no puede contener mas de 30 dígitos<br>";
            entrar = false;
        }

        if ((pass1.length > 60 || pass1.length < 4) || (pass2.length > 60 || pass2.length < 4)) {
            mensajeMostrar += "La contraseñas deben tener entre 4 y 60 caracteres<br>";
            entrar = false; 
        }

        if (!(isUpper(pass1) || isUpper(pass2))) {
            mensajeMostrar += "Una letra de las contraseñas debe ser mayúscula<br>";
            entrar = false;
        }

        if (!tieneNumero(pass1) || !tieneNumero(pass2)) {
            mensajeMostrar += "Un dígito de las contraseñas debe ser un número<br>";
            entrar = false;
        }


        if (pass1 != pass2) {
            mensajeMostrar += "Las contraseñas no coinciden<br>";
            entrar = false;
        }
        if (entrar) {
            $("#mensajeReg").html("Cargando...");
        }
        else {
            $("#mensajeReg").html(mensajeMostrar);
            e.preventDefault();
        }
    });
})

function esMayuscula(letra) {
    return letra == letra.toUpperCase();
};

function isUpper(str) {
    return /[A-Z]/.test(str);
}

function tieneNumero(numero) {
    return /\d/.test(numero);
}