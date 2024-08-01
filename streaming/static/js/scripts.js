document.addEventListener("DOMContentLoaded", function () {

    // Mobile Navigation Menu Toggle
    const menuButton = document.querySelector(".menu-button");
    const navMenu = document.querySelector("header nav");

    if (menuButton) {
        menuButton.addEventListener("click", () => {
            navMenu.classList.toggle("active");
        });
    }
});
