document.addEventListener('DOMContentLoaded', function() {
    const facebookIcon = document.querySelector('.facebook-icon i');

    //animación al icono
    facebookIcon.addEventListener('mouseenter', function() {
        facebookIcon.style.animation = 'shake 0.5s ease-in-out';
    });

    facebookIcon.addEventListener('animationend', function() {
        facebookIcon.style.animation = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const facebookIcon = document.querySelector('.facebook-icon');

    facebookIcon.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = 'https://www.facebook.com/p/Oficial-T%C3%A9cnica-No-26-Zaragoza-Huamantla-Tlax-100063554410845/?locale=es_LA'; // Reemplaza con tu URL de Facebook
    });
});

