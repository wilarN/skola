
car = {
    "Model": "Toyota",
    "Year": 2022,
    "Colour": "White",
    "Owner": "William"
};

document.writeln(car.Model);
document.writeln(car.Year);
document.writeln(car.Colour);
document.writeln(car.Owner);


function myFunc() {
    "use strict"; document.writeln(prompt("First num: ")/prompt("First num: "));
}

let student = {
    "firstName": "Hampus",
    age: 23
};

let person = {
    "stdName": "Hilda",
    "age": 15,
};

// alert(person["stdName"] + " är " + person["age"]);

// let celcius = 19;
// console.log((1.8 * celcius)+32);

// let usrName = prompt("Whats your name?: ");
// alert("Welcome " + usrName + "!");

//function masterFunc(param) {
//    alert(param)
//}
function masterFunc(){
    alert(prompt("Num1: ") * prompt("Num2: "))
}
masterFunc();