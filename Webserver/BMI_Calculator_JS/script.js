// BMI-Calculator

// BMI = weight / height^2

function bmiCalculator(weight, height) {
    // To the nearest whole number
    return Math.round(weight / Math.pow(height, 2));
}

console.log("BMI: " + bmiCalculator(70, 1.8));

// Love score struct
// 0-20% - Not a chance.
// 21-50% - Maybe???
// 51-80% - Perchance...
// 81-100% - Made for each other!
const scores = {
    "0-20": "Not a chance.",
    "21-50": "Maybe???",
    "51-80": "Perchance...",
    "81-100": "Made for each other!"
}


function loveCalculator(event) {
    event.preventDefault();

    let firstPerson = document.getElementById("fname").value;
    let secondPerson = document.getElementById("sname").value;
    let result = document.getElementById("result");
    let extra = document.getElementById("extra");

    extra.removeAttribute("class");

    if(firstPerson === "" || secondPerson === "") {
        result.innerHTML = "Please enter both names.";
        return;
    }

    // Randomize 1-100
    var loveScore = Math.random() * 100;
    // Round to nearest integer
    loveScore = Math.round(loveScore);
    let extraComment = "";
    if(loveScore < 21){     
        extraComment = scores["0-20"];
        extra.classList.add("text-danger");
    }else if(loveScore >= 21 && loveScore < 51){
        extra.classList.add("text-warning");
        extraComment = scores["21-50"];
    }else if(loveScore < 81 && loveScore > 50){
        extra.classList.add("text-success");
        extraComment = scores["51-80"];
    }else if(loveScore > 80 ){
        extra.classList.add("text-success");
        extraComment = scores["81-100"];
    }
    extra.innerHTML = extraComment;
    result.innerHTML = firstPerson + " & " + secondPerson + "'s love for each other is at " + loveScore + "%";

}

//bmiCalculator(70, 180);

//loveCalculator();