
// Función para obtener una broma
function obtenerBroma() {
    // URL de la API
    const apiUrl = 'https://icanhazdadjoke.com/';
    // Realizar la solicitud GET a la API
    fetch(apiUrl, {
        headers: {
            'Accept': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            // Extraer la broma del objeto de respuesta
            const broma = data.joke;
            // Mostrar la broma en la página
            document.getElementById('BROMA').innerText = broma;
        })
        .catch(error => {
            console.error('Error al obtener la broma:', error);
        });
  }
  // Obtener la broma cuando se hace clic en el botón
  document.addEventListener('DOMContentLoaded', function() {
      obtenerBroma();
      // Asegurarse de que el contenido de CERTIFICADET sea visible en la página
      document.getElementById('CERTIFICADET').scrollIntoView();
  });