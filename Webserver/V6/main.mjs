import inquirer from "inquirer"; // Importerar inquirer
import qr from "qr-image"; // Importerar qr-image
import fs from "fs"; // Importerar fs
import sillynames from "sillyname"; // Importerar sillyname
import superheroes from "superheroes"; // Importerar superheroes

// UPPGIFT 1 (hälsning)
console.log("Hello World");

// UPPGIFT 2 (spara ner en textfil)
fs.writeFile("hello.txt", "Hello World!", (err) => {
    if (err) throw err;
    console.log("The file has been saved!");
});

// UPPGIFT 3 (sillynames)
console.log("My silly name is " + sillynames() + "!");

// UPPGIFT 3 Fortsättning (superheroes)
console.log("My superhero name is " + superheroes.random() + "!");



// UPPGIFT 4 (inquirer & qr-image för att skapa en QR-kod från en URL)
function randomChars(length) {
    // För att skapa en unik filnamn för svg-filen
    let result = "";
    let characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    // Loopar efter length
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

// Frågar efter en URL
inquirer.prompt([
    {
        type: "input",
        message:"What url do you want to convert to QR code?",
        name: "url"
    }
])
    // Skapa en QR-kod från URLen som togs in
    .then((Answers) => {
        // SVG format
        let qr_svg = qr.image(Answers['url'], { type: "svg" });
        // Sparar ner svg-filen på disk
        let tmpFileName = `${randomChars(5)}`;
        qr_svg.pipe(fs.createWriteStream(`${tmpFileName}.svg`));
        console.log("QR code saved as svg as: " + tmpFileName + ".svg");
    })
    // Error hantering
    .catch((error) => {
        if (error.isTtyError) {
            console.log("Prompt couldn't be rendered in the current environment");
            console.log(error);
        } else {
            console.log("Something went wrong");
            console.log(error);
        }
    });
