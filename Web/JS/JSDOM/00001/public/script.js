
let btn = document.getElementsByTagName("button");

for(let i = 0; i < btn.length; i++){
    btn[i].style.backgroundColor = "orange";
    btn[i].style.width = "100px";
    btn[i].style.height = "50px";
}

let queryElem = document.querySelector("h2");
queryElem.style.color = "red";
queryElem.style.fontSize = "3rem";

let todoItemID = document.querySelectorAll(".to-do-item");
for(let i = 0; i < todoItemID.length; i++){
    todoItemID[i].style.backgroundColor = "black";
    todoItemID[i].style.color = "white";
    todoItemID[i].style.fontSize = "2rem";
    todoItemID[i].style.border = "2px solid white";
    todoItemID[i].style.boxShadow = "0px 0px 10px white";
    todoItemID[i].style.borderRadius = "10px";
}


let ClassElem = document.getElementsByClassName("to-do-item");
for(let i = 0; i < ClassElem.length; i++){
    ClassElem[i].style.color = "greenyellow";
    ClassElem[i].style.fontSize = "2rem";
}

function showCurTime(){
    let date = new Date();
    alert(date);
}