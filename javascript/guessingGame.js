
const prompt = require("prompt-sync")({ sigint: true });

let randNum = parseInt(Math.random() * 100);
var counter = 0;
var succeed = false;

console.log(randNum, typeof randNum);
while (counter < 10) {
    var guess = parseInt(prompt("Enter your guess: "));
    console.log(guess, typeof guess);
    if (guess > randNum) {
        console.log("Guess lower.");
    } else if (guess < randNum) {
        console.log("Guess higher.");
    }
    else {
        console.log("Congragulation; You win ${counter} attempts.");
        succeed = true;
        break;
    }
    counter++;
}

if (!succeed) {
    console.log("Sorry you didn't get it. Maybe next time!!");
}