const carousel = document.querySelector('.carousel-track');
const items = document.querySelectorAll('.carousel-item');
const totalSlides = items.length - 1; // Total slides excluding duplicate
let index = 0;
let delay = 1000; // 1-second delay after each transition

// Function to show the next slide
function showNextSlide() {
    index++; // Move to the next slide

    if (index > totalSlides) {
        // If at the duplicate slide, reset to the first slide without animation
        setTimeout(() => {
            carousel.style.transition = 'none'; // Disable transition
            index = 0; // Reset to the first slide
            carousel.style.transform = `translateX(0%)`;
        }, 1000); // Delay before resetting
    } else {
        // Smooth transition to the next slide
        carousel.style.transition = 'transform 1s ease-in-out';
        carousel.style.transform = `translateX(-${index * 100}%)`;
    }
}

// Autoplay the carousel
function startAutoplay() {
    setInterval(showNextSlide, 3000); // 3 seconds per slide
}

// Start autoplay
startAutoplay();
