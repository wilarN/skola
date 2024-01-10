


// All available menu items
const menuItems = [
    { id: 1, name: "Sashimi Mikado", price: 175 },
    { id: 2, name: "Sashimi Shake", price: 175 },
    { id: 3, name: "Tempura Moriwase", price: 175 },
    { id: 4, name: "Syo Zin Age", price: 105 },
    { id: 5, name: "Agedashi-Tofu", price: 105 },
    { id: 6, name: "Ise-Ebi", price: 295 },
    { id: 7, name: "Hotategai Furai", price: 190 },
    { id: 8, name: "Taisho-Ebi", price: 175 },
    { id: 9, name: "Yakitori", price: 120 },
    { id: 10, name: "Harumaki", price: 105 },
    { id: 11, name: "8 sorterade bitar", price: 160 },
    { id: 12, name: "10 sorterade bitar", price: 180 },
    { id: 13, name: "extra valfri bit", price: 17 },
    { id: 14, name: "Tempura Maki", price: 215 },
    { id: 15, name: "Fusion Makirulle", price: 195 },
    { id: 16, name: "Dragon Makirulle", price: 195 },
    { id: 17, name: "Rainbow Makirulle", price: 195 },
    { id: 18, name: "Shio Yaki Makirulle", price: 195 },
    { id: 19, name: "Yakiniku Makirulle", price: 215 },
    { id: 20, name: "California Makirulle", price: 160 },
    { id: 21, name: "Purjolök Makirulle", price: 160 }
];

let my_order = [];

let priceToPay = document.getElementById("pricetopay").innerHTML = "0";

if(my_order.length === 0){
    document.getElementsByClassName("cart-items-total")[0].style.display = "none";
}

function addCartItem(itemID){
    const item = menuItems.find(item => item.id === itemID);
    if(item){
        my_order.push(item);
        renderCart();
    }
}

function renderCart(){
    if(my_order.length >0){
        document.getElementsByClassName("cart-items-total")[0].style.display = "flex";
    }

    let price = 0;
    my_order.forEach(item => {
        price += item.price;
    });

    document.getElementById("pricetopay").innerHTML = price;
    renderCartInDOM();
}

function renderCartInDOM() {
    // Tack till chatgpt för denna funktionen! (: <3
    const cartContainer = document.getElementById('cart-container');
    cartContainer.innerHTML = ''; // Clear previous content

    if (my_order.length > 0) {
        const ul = document.createElement('ul');
        my_order.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.name} - ${item.price} kr`;
            ul.appendChild(li);
        });
        cartContainer.appendChild(ul);
    } else {
        cartContainer.textContent = 'Your cart is empty.';
    }

    // Update price to pay
    
}

function removeCartItem(itemID){
    const item = menuItems.find(item => item.id === itemID);
    if(item){
        my_order.splice(my_order.indexOf(item), 1);
        renderCart();
    }
}



document.addEventListener("DOMContentLoaded", () => {
    const menuLinks = document.querySelectorAll(".menu-item a");
    menuLinks.forEach(link => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            const itemID = parseInt(link.dataset.itemId, 10);
            console.log(itemID);
            addCartItem(itemID);
        });
    });
});



function print_cart_to_console(){
    console.log(my_order);
}

//Thread loop for printing cart to console
setInterval(print_cart_to_console, 1000);