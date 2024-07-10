const historiaImg = document.getElementById('historia-img');
const imagenes = [
    '/static/img/historia1.png',
    '/static/img/historia2.png'
];
let indice = 0;

function cambiarImagen() {
    historiaImg.style.opacity = 0; 
    setTimeout(() => {
        historiaImg.src = imagenes[indice]; 
        historiaImg.style.opacity = 1; 
    }, 200);
    indice = (indice + 1) % imagenes.length; 
}

setInterval(cambiarImagen, 4000); 

