// let username = prompt("Please enter your name: ");

// document.getElementById('usrn').innerHTML = username;

let password = "awesomepassword";
let attempts = 0;


document.getElementById('profPic').style.boxShadow = "2px 2px 30px cyan";

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

function passwordCheck(){
    attempts +=1;
    let usr_try_pass = document.getElementById('passInput').value;
    console.log(usr_try_pass);
    if (document.getElementById("status").style.display === "none" || document.getElementById("att").style.display === "none"){
        document.getElementById("status").style.display = "block";
        document.getElementById("att").style.display = "block";  
    }
    if(usr_try_pass == password){
        document.getElementById('result').innerHTML = "Logged in.";
        document.getElementById('profPic').style.boxShadow = "2px 2px 30px green";
        document.getElementById('profPic').style.height = "3000px";
        document.getElementById('bigpic').style.display='block';
    } else{
        document.getElementById('result').innerHTML = "Wrong password";
        document.getElementById('profPic').style.boxShadow = "2px 2px 30px red";
        document.getElementById('profPic').style.height = "100px";
    }

    document.getElementById('attempts').innerHTML = attempts;


}