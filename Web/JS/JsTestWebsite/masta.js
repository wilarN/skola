
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }

function masta_epico() {
    for (let index = 0; index < 10; index++) {
        document.getElementById("mast").innerHTML = document.getElementById("mast").innerHTML + "A";
        setTimeout(50);
    }
}

document.onload(masta_epico());