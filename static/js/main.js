document.addEventListener('DOMContentLoaded', function() {
    const title = document.querySelector('.contenido h2');
    const subtitle = document.querySelector('.contenido p');
    const videoButton = document.getElementById('videoButton');
    const videoContainer = document.getElementById('videoContainer');
    const closeVideoButton = document.getElementById('closeVideoButton');
    const video = document.querySelector('.video-container video');

    function fadeInUp(element) {
        element.style.opacity = '1';
        element.style.transform = 'translateY(0)';
    }


    fadeInUp(title);
    setTimeout(function() {
        fadeInUp(subtitle);
    }, 300);

    videoButton.classList.add('animate');
});
