const form = document.getElementById('formulario_contacto')
const nombre = document.getElementById('id_nombreContacto')
const email = document.getElementById('id_emailContacto')
const telefono = document.getElementById('id_telefonoContacto')
const comentario = document.getElementById('id_comentarioContacto')

form.addEventListener('submit', (event) => {

    event.preventDefault();
  
    if (!form.checkValidity()) {
      event.stopPropagation();
    }
  
    form.classList.add('was-validated');

});


nombre.addEventListener('input', () => {
    if (nombre.validity.valid) {
      nombre.classList.remove('is-invalid');
    } else {
      nombre.classList.add('is-invalid');
    }
});

email.addEventListener('input', () => {
    if (nombre.validity.valid) {
      nombre.classList.remove('is-invalid');
    } else {
      nombre.classList.add('is-invalid');
    }
});

telefono.addEventListener('input', () => {
    if (nombre.validity.valid) {
      nombre.classList.remove('is-invalid');
    } else {
      nombre.classList.add('is-invalid');
    }
});

comentario.addEventListener('input', () => {
    if (nombre.validity.valid) {
      nombre.classList.remove('is-invalid');
    } else {
      nombre.classList.add('is-invalid');
    }
});