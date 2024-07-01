document.getElementById('generateBtn').addEventListener('click', function() {
    // Número de usuarios que deseas generar
    const numUsers = 3; // Por ejemplo, generar 3 usuarios

    // Array para almacenar las promesas de las solicitudes fetch
    const promises = [];

    // Array de comentarios inicial
    let comments = [
        "Muy buen servicio, tuve un problema y lo resolvieron a la brevedad",
        "Excelente atención al cliente, me ayudaron con mi consulta de manera eficiente",
        "¡Gracias por la ayuda! El servicio fue rápido y profesional",
        "Aun que se demoraron en responder, lo lograron solucionar muy rapido",
        "No puedo decir mucho sobre lo visual de la pagina, pero todo sirve muy bien",
        "Saben porque se extinguieron los mamuts? porque no habian paputs",
        "No puedo creer lo mal que estan diseñadas ciertas vistas de esta pagina"
    ];

    // Función para seleccionar y eliminar un comentario aleatorio del array
    function getRandomComment() {
        const randomIndex = Math.floor(Math.random() * comments.length);
        const randomComment = comments[randomIndex];
        comments.splice(randomIndex, 1); // Eliminar el comentario seleccionado
        return randomComment;
    }

    // Hacer múltiples solicitudes fetch
    for (let i = 0; i < numUsers; i++) {
        promises.push(
            fetch('https://randomuser.me/api/')
            .then(response => response.json())
            .then(data => {
                const user = data.results[0];
                const randomComment = getRandomComment(); // Obtener un comentario aleatorio
                return { user, comment: randomComment }; // Retornar el usuario y el comentario
            })
        );
    }

    // Esperar a que todas las solicitudes fetch se completen
    Promise.all(promises)
    .then(usersWithComments => {
        let userDetails = '';

        // Construir los detalles de cada usuario con su comentario
        usersWithComments.forEach(({ user, comment }) => {
            userDetails += `
                <div class="user">
                    <img src="${user.picture.large}" alt="User Image">
                    <div class="user-info">
                        <p>${user.name.first} ${user.name.last}</p>
                        <p><strong>${comment}</strong></p>
                    </div>
                </div>
            `;
        });

        // Agregar los detalles de los usuarios al contenedor userDetails
        document.getElementById('userDetails').innerHTML = userDetails;
    })
    .catch(error => console.error('Error fetching users:', error));
});