

function main_func(){
const countries = ["Sweden", "Denmark", "Finland", "France"];
console.log(countries);

const Colours = ["Green", "Yellow", "Red", "Blue", "Purple"];
console.log(Colours);

Colours.unshift("Orange");
console.log(Colours);

Colours.splice(2, 1);
console.log(Colours);


const Cities = ["Göteborg", "Stockholm", "Malmö", "Uppsala", "Jönköping"];

Cities.unshift("Upplandsväsby");
console.log(Cities);

Cities.splice(4, 1);
console.log(Cities);

Cities.splice(5, 0, "Örebro");
console.log(Cities);

Cities.unshift("Venedig");
console.log(Cities);

}