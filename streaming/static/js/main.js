document.addEventListener('DOMContentLoaded', (event) => {
    const modeSwitcher = document.getElementById('modeSwitcher');
    const currentMode = localStorage.getItem('theme') || 'light-mode';

    // Set the current theme of the page
    document.body.classList.add(currentMode);
    updateModeSwitcherText(currentMode);

    // Theme toggle
    modeSwitcher.addEventListener('click', () => {
        const newMode = document.body.classList.contains('light-mode') ? 'dark-mode' : 'light-mode';
        toggleTheme(newMode);
    });

    document.addEventListener('DOMContentLoaded', () => {
        const modeSwitcher = document.getElementById('modeSwitcher');
    
        modeSwitcher.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            if (document.body.classList.contains('dark-mode')) {
                modeSwitcher.textContent = 'Switch to Light Mode';
            } else {
                modeSwitcher.textContent = 'Switch to Dark Mode';
            }
        });
    });
    

    // Toggle theme and update text
    function toggleTheme(newMode) {
        document.body.classList.remove('light-mode', 'dark-mode');
        document.body.classList.add(newMode);
        localStorage.setItem('theme', newMode);
        updateModeSwitcherText(newMode);
    }

    // Update the button text to switch modes
    function updateModeSwitcherText(mode) {
        modeSwitcher.textContent = mode === 'light-mode' ? 'Switch to Dark Mode' : 'Switch to Light Mode';
    }
});
