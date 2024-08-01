document.addEventListener("DOMContentLoaded", function () {
    // // JavaScript kodlarını /* `buraya` is a Turkish word that translates to "here" in English. In the
    // given context, it is used as a placeholder to indicate that JavaScript
    // code can be added in that specific location within the
    // `addEventListener` function. It is a common practice to use placeholders
    // like `buraya` to guide where certain code should be inserted or written. */
    //  buraya ekleyebilirsiniz.
    //  Örneğin: Dinamik arama, kullanıcı etkileşimleri vb.

    // Mobile Navigation Menu Toggle
    const menuButton = document.querySelector(".menu-button");
    const navMenu = document.querySelector("header nav");

    if (menuButton) {
        menuButton.addEventListener("click", () => {
            navMenu.classList.toggle("active");
        });
    }
});
