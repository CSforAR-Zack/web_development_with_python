function countdownTimer(seconds, id) {
    var timeLeft = parseInt(seconds, 10);
    var x = setInterval(function() {
        var countdownElement = document.getElementById(id);

        if (timeLeft <= 0) {
            countdownElement.style.color = "red";
            countdownElement.innerHTML =  "TIME IS UP!";
            clearInterval(x);
            return;
        }
        countdownElement.innerHTML = timeLeft;
        timeLeft--;
    }, 1000);
}

function scrambleGlitch(className) {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const element = document.querySelector(className);
    const speed = 50;
    const cycles = 1/3;

    element.onmouseover = event => {
        const target = event.target;
        const originalText = target.dataset.value;
        const splitText = originalText.split("");
        let iteration = 0;

        const interval = setInterval(() => {
            target.innerText = splitText.map(
                (char, index) => {
                    if (index < iteration) {
                        return char;
                    }
                    return letters[Math.floor(Math.random() * letters.length)];
                }
            ).join("");

            if (iteration >= originalText.length) {
                clearInterval(interval);
            }

            iteration += cycles;
        }, speed);
    };
}