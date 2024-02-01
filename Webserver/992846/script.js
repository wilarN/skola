

/* Uppgiften om vem som är tillåten till partyt.  */
var guestList = ["Angela", "Jack", "Pam", "James", "Lara", "Jason"];

var guestName = prompt("What is your name?");
guestName = guestName.charAt(0).toUpperCase() + guestName.slice(1);
if (guestList.includes(guestName)) {
    alert("Welcome to the party " + guestName + "!");
}
else {
    alert("Sorry, you're not on the list, maybe next time.");
}

// ---------------------------------------------------------------

/* Guest list  */

var guestList = ["Angela", "Jack", "Pam", "James", "Lara", "Jason"];

function getWhoPays(list){
    let randomNum = Math.floor(Math.random() * list.length);
    return list[randomNum];
}

// Den som får betala
console.log("Idag betalar " + getWhoPays(guestList));

// ---------------------------------------------------------------


/* Fizzbuzz uppgiften */
let keepTrack = [];

for (let i = 0; i < 100; i++) {
    let randomNum = Math.floor(Math.random() * 100);

    if (randomNum % 3 === 0 && randomNum % 5 === 0) {
        keepTrack.push("FizzBuzz");
    } else if (randomNum % 3 === 0) {
        keepTrack.push("Fizz");
    } else if (randomNum % 5 === 0) {
        keepTrack.push("Buzz");
    } else {
        keepTrack.push(randomNum);
    }
}
console.log(keepTrack);

// ---------------------------------------------------------------


// /* 99 bottles of beer on the wall uppgiften */
// function LyricsPlaceholder(number){
//     let textPlaceholder = `${number} bottles of beer on the wall, ${number} bottles of beer. Take one down and pass it around, ${number} bottles of beer on the wall.`;
//     return textPlaceholder;
// }

// for (let i = 100; i >= 0; i--) {
//     if(i === 1){
//         console.log("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.");
//     }else if(i === 0){
//         console.log("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.");
//     }else{
//         console.log(LyricsPlaceholder(i));
//     }
// }

// ---------------------------------------------------------------

/* Fibonacci uppgiften */

function fibonacciGenerator(n) {
    let output = [];
    if (n === 1) {
        output = [0];
    } else if (n === 2) {
        output = [0, 1];
    } else {
        output = [0, 1];
        for (let i = 2; i < n; i++) {
            output.push(output[output.length - 2] + output[output.length - 1]);
        }
    }
    return output;
}

console.log(fibonacciGenerator(50));


// ---------------------------------------------------------------