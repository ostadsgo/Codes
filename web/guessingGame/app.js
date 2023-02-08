
let randNumber = Math.random() * 100;
var counter = 0;

function onGuess() {
    let guessInput = document.getElementById("userGuess");
    let guessValue = guessInput.value;
    let guess = parseInt(guessValue);
    var result = document.getElementById("result");
    // var succeed = false;

    if (guess > randNumber) {
        result.innerHTML = "Try lower.";
    }
    else if (guess < randNumber) {
        result.innerHTML = "Try higher";
    }
    else {
        result.innerHTML = "Congragulation; You did it $counter attempts.";
        succeed = true;
    }
    guessInput.value = "";
    counter++;
}

