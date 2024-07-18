$(document).ready(function() {
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        navText: [
            '<span class="carousel-control-prev-icon" aria-hidden="true"></span>',
            '<span class="carousel-control-next-icon" aria-hidden="true"></span>'
        ],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    });
});
