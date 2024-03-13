// const new_element = document.createElement('a');
// const parent_elem = document.getElementById('div1');
// const div1 = document.getElementById('div1');
// new_element.href = "https://www.meltrasense.xyz";
// new_element.target = "_blank";
// new_element.innerHTML = "meltrasense";
// div1.insertBefore(new_element, div1.children[1]);
// div1.removeChild(div1.children[0]);

const myElem = document.createElement("div.myDiv");
const oldSpan = document.getElementById("oldSpan");
const newSpan = document.createElement("span");
const existingDiv = document.getElementsByClassName("existingDiv")[0];
newSpan.innerHTML = "Detta är den nya texten";
myElem.innerHTML = "Detta är min div";

oldSpan.replaceWith(newSpan);

const newP = document.createElement("p");
newP.id = "newPara";

existingDiv.appendChild(newP);
let WWidth = window.innerWidth;
let WHeight = window.innerHeight;
console.log(WWidth + "px x " + WHeight + "px");
window.open("https://www.meltrasense.xyz", "_blank", "width=200, height=100");

// GM
const canvas = document.createElement("myCanvas"); 
window.ctx = canvas.getContext("2d");
ctx.fillStyle = "blue";
ctx.fillRect(0, 0, 150, 75);