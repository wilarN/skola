import inquirer from "inquirer";
import qr from "qr-image";
import fs from "fs";
import sillynames from "sillyname";
import superheroes from "superheroes";

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

// UPPGIFT 4 (inquirer)


function randomChars(length) {
    let result = "";
    let characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

inquirer.prompt([
    {
        type: "input",
        message:"What url do you want to convert to QR code?",
        name: "url"
    }
])
    .then((Answers) => {
        console.log(Answers);
        let qr_svg = qr.image(Answers['url'], { type: "svg" });
        qr_svg.pipe(fs.createWriteStream(`${randomChars(5)}.svg`));
        let svg_string = qr.imageSync("I love QR!", { type: "svg" });
    })
    .catch((error) => {
        if (error.isTtyError) {
            console.log("Prompt couldn't be rendered in the current environment");
            console.log(error);
        } else {
            console.log("Something went wrong");
            console.log(error);
        }
    });
