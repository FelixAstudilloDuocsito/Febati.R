function validacionSop(){
    var VarNom = false;
    var VarCor = false;
    var VarPro = false;
    
    var nombre = document.getElementById("nombre").value;
    var correo = document.getElementById("correo").value;
    var Prob = document.getElementById("Prob").value;
    
    //se verifica el nombre ingresado
    if (nombre === "") {
        document.getElementById("mensaje1").textContent = "Debe ingresar su nombre ";
    } else if (nombre.length < 3 || nombre.length > 14) {
        document.getElementById("mensaje1").textContent = "El nombre debe tener entre 3 y 14 caracteres";
    } else {
        VarNom = true;
        // Restablecer mensajes de error
        document.getElementById("mensaje1").textContent = "";
    }
    //se verifica el correo
    if (correo === "") {
        document.getElementById("mensaje2").textContent = "Debe ingresar un correo ";
    } else if (!correo.includes('@')) {
        document.getElementById("mensaje2").textContent = "El correo electrónico debe contener '@'";
    } else if (!/@[^\s@]+$/.test(correo)) {
        document.getElementById("mensaje2").textContent = "Después del '@' debe haber al menos un caracter";
    } else if (!correo.includes('.')) {
        document.getElementById("mensaje2").textContent = "El correo electrónico debe contener '.' después del '@'";
    } else if (!/\.[^\s@]+$/.test(correo)) {
        document.getElementById("mensaje2").textContent = "Después del último punto debe haber al menos un caracter";
    } else {
        VarCor = true;
        // Restablecer mensajes de error
        document.getElementById("mensaje2").textContent = "";
    }
    //Se verifica el mensaje de la problematica 
    if (Prob === "") {
        document.getElementById("mensaje3").textContent = "El problema no puede estar vacío ";
    } else if (Prob.length < 20 || Prob.length > 500) {
        document.getElementById("mensaje3").textContent = "El problema tiene que tener un mínimo de 20 caracteres y un máximo de 500";
    } else {
        VarPro = true;
        // Restablecer mensajes de error
        document.getElementById("mensaje3").textContent = "";
    }
    if (VarNom && VarCor && VarPro) { 
        //mensaje de problema enviado
        document.getElementById("mensaje4").textContent = "¡El problema a sido enviado y se le respondera a la brevedad!";
    }
}