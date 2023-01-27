// let username = prompt("Please enter your name: ");

// document.getElementById('usrn').innerHTML = username;

let password = "awesomepassword";
let attempts = 0;

passwordPrompt();

function passwordPrompt(){
    attempts +=1;
    let result = prompt("Enter password: ")
    while(true){   
        if(result == password){
            document.getElementById('result').innerHTML = "Logged in.";
            document.getElementById('bigpic').style.display='block';
        } else{
            document.getElementById('result').innerHTML = "Wrong password";
            break;
        }
    }
    document.getElementById('attempts').innerHTML = attempts;
}
