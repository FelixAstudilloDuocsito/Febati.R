function validacionLog(){
    VarUs = false
    VarCon = false
    var usuario = document.getElementById("usuario").value;
    var contrasena = document.getElementById("contrasena").value;

    //Verifica el usuario 
    if (usuario === "") {
        document.getElementById("mensaje1").textContent = "Debe ingresar un nombre de usuario ";
    } else if (usuario.length < 3 || usuario.length > 14) {
        document.getElementById("mensaje1").textContent = "El usuario debe tener entre 3 y 14 caracteres";
    } else {
        VarUs = true;
        //restrablecer mensajes de error
        document.getElementById("mensaje1").textContent = "";
    }
    //Verifica la contraseña 
    if (contrasena === "") {
        document.getElementById("mensaje2").textContent = "Debe ingresar una contraseña  ";
    } else if (contrasena.length < 8 || contrasena.length > 16) {
        document.getElementById("mensaje2").textContent = "La contraseña debe tener entre 8 y 16 caracteres";
    } else {
        VarCon = true;
        document.getElementById("mensaje2").textContent = "";
    }
    //Redirije a la pagina principal 
    if (VarUs===true&&VarCon===true)
        { 
        location.href="/CS/";
    }
     
}
