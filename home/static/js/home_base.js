const mobileMenu = document.getElementById('mobile-menu');
const navContent = document.querySelector('.nav-content');

mobileMenu.addEventListener('click', () => {
    navContent.classList.toggle('show');
});

// this is for custome cursor
const cursor = document.querySelector(".cursor");
var timeout;

document.addEventListener("mousemove", (e) => {
    let x = e.clientX;
    let y = e.clientY;

    cursor.style.top = y + "px";
    cursor.style.left = x + "px";
    cursor.style.display = "block";

    function mouseStopped() {
        cursor.style.display = "none";
    }
    clearTimeout(timeout);
    timeout = setTimeout(mouseStopped, 5000);
});

document.addEventListener("mouseout", () => {
    cursor.style.display = "none";
});



