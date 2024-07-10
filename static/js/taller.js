document.addEventListener('DOMContentLoaded', function() {
    var moreInfoBtns = document.querySelectorAll('.more-info-btn');

    moreInfoBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var moreInfo = this.parentElement.querySelector('.more-info');
            var mainImage = this.parentElement.parentElement.querySelector('.main-image');
            var otherImage = this.parentElement.parentElement.querySelector('.other-image');

            moreInfo.classList.toggle('active');
            if (moreInfo.classList.contains('active')) {
                mainImage.classList.add('d-none');
                otherImage.classList.remove('d-none');
                this.textContent = 'Ocultar';
            } else {
                mainImage.classList.remove('d-none');
                otherImage.classList.add('d-none');
                this.textContent = 'Ver más';
            }
        });
    });
});
