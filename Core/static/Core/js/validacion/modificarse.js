$(document).ready(function () {

    $("#formRegi").submit(function (e) {
        
        
        var nombre = $("#nombre1").val();
        var ape = $("#apellido1").val();
        var nick = $("#username1").val();
        var mail = $("#email1")

      

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

        if (mail.length > 70) {
            mensajeMostrar += "El correo no puede contener mas de 70 dígitos<br>";
            entrar = false;
        }

        

        if (entrar) {
            $("#mensajeReg").html("Cargando...");
        }
        else {
            e.preventDefault();
            $("#mensajeReg").html(mensajeMostrar);
            
        }
    });
})

function esMayuscula(letra) {
    return letra == letra.toUpperCase();
};

function isUpper(str) {
    return /[A-Z]/.test(str);
}

