// Counts down from `seconds` to 0 inside the element with the given id,
// then shows "TIME IS UP!" in red.
function countdownTimer(seconds, id) {
    let timeLeft = parseInt(seconds, 10);
    const el = document.getElementById(id);

    const timer = setInterval(() => {
        if (timeLeft <= 0) {
            el.style.color = "red";
            el.innerHTML = "TIME IS UP!";
            clearInterval(timer);
            return;
        }
        el.innerHTML = timeLeft--;
    }, 1000);
}

// On hover, scrambles the element's text into random letters, then
// "locks in" the real letters one by one, left to right.
function scrambleGlitch(className) {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const randomLetter = () => letters[Math.floor(Math.random() * letters.length)];
    const element = document.querySelector(className);

    element.onmouseover = ({ target }) => {
        const text = [...target.dataset.value];
        let locked = 0;

        const timer = setInterval(() => {
            target.innerText = text.map((char, i) => (i < locked ? char : randomLetter())).join("");
            locked += 1 / 3; // fractional step = ~3 frames per letter
            if (locked >= text.length) clearInterval(timer);
        }, 50);
    };
}
