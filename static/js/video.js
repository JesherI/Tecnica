document.addEventListener('DOMContentLoaded', function() {
    const videoButton = document.getElementById('videoButton');
    const videoContainer = document.getElementById('videoContainer');
    const closeVideoButton = document.getElementById('closeVideoButton');
    const video = document.querySelector('.video-container video');

    videoButton.addEventListener('click', function() {
        videoContainer.style.display = 'block';
        video.play();
    });

    closeVideoButton.addEventListener('click', function() {
        videoContainer.style.display = 'none';
        video.pause(); 
        
    });
});
