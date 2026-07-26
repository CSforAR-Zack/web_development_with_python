const themeToggle = document.getElementById("theme-toggle");

themeToggle.addEventListener("click", (event) => {
    event.preventDefault();

    // Flip the theme instantly, no page reload
    document.documentElement.classList.toggle("light-mode");

    // Logged-in users get their choice saved server-side in the background
    const syncUrl = themeToggle.getAttribute("href");
    if (syncUrl) {
        fetch(syncUrl, { method: "GET", credentials: "same-origin" }).catch(() => {});
    }
});
