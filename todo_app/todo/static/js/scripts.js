const themeBtn = document.getElementById("theme-toggle");

themeBtn.addEventListener("click", () => {
    // Toggle the override class on the body
    document.body.classList.toggle("light-mode");
    
    // Update the button text so it makes sense
    if (document.body.classList.contains("light-mode")) {
        themeBtn.innerText = "Switch to Dark Mode";
    } else {
        themeBtn.innerText = "Switch to Light Mode";
    }
});