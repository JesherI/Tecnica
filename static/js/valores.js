function toggleLike(button) {
    button.classList.toggle('active'); 
    var heartIcon = button.querySelector('i');

   
    if (button.classList.contains('active')) {
        heartIcon.classList.remove('far');
        heartIcon.classList.add('fas');
        heartIcon.style.color = '#80052e'; 
    } else {
        heartIcon.classList.remove('fas');
        heartIcon.classList.add('far');
        heartIcon.style.color = '#361219'; 
    }
    
    var valorId = button.parentNode.querySelector('.card-title').textContent.trim().toLowerCase(); 
    var likes = JSON.parse(localStorage.getItem('likes')) || {};
    
    likes[valorId] = button.classList.contains('active');
    
    localStorage.setItem('likes', JSON.stringify(likes));
}

document.addEventListener('DOMContentLoaded', function() {
    var likes = JSON.parse(localStorage.getItem('likes')) || {}; 
    
    // Itera sobre los likes y establece el estado activo en los botones correspondientes
    Object.keys(likes).forEach(function(valorId) {
        var button = document.querySelector('.card-title:contains("' + valorId + '")').parentNode.querySelector('.like-button');
        if (likes[valorId]) {
            button.classList.add('active');
            var heartIcon = button.querySelector('i');
            heartIcon.classList.remove('far');
            heartIcon.classList.add('fas');
            heartIcon.style.color = '#80052e'; 
        }
    });
});
