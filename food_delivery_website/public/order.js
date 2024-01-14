
import { menuItems } from './menu.js';

let my_order = [];

let priceToPay = document.getElementById("pricetopay").innerHTML = "0";
let orderCheckOutContainer = document.getElementsByClassName("order-checkout-container")[0];
orderCheckOutContainer.style.display = "none";


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
        orderCheckOutContainer.style.display = "flex";
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
            // X for removing item from cart
            const removeButton = document.createElement('button');
            removeButton.textContent = 'X';
            removeButton.addEventListener('click', () => {
                removeCartItem(item.id);
            });
            li.appendChild(removeButton);
        });
        cartContainer.appendChild(ul);
    } else {
        cartContainer.textContent = 'Your cart is empty.';
    }

    // Update price to pay
    
}


// Removes item from cart
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

// Adds all items in cart to get param for the checkout page
function addAllToGetParam(){
    let getParam = "?";
    my_order.forEach(item => {
        getParam += item.id + "&";
    });
    getParam = getParam.slice(0, -1);
    return getParam;
}

// Adds all items in cart to get param for the checkout page -
// when checkout href is interacted with.
document.addEventListener("DOMContentLoaded", () => {
    const toCheckout = document.querySelectorAll("#to-checkout");
    toCheckout.forEach(link => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            let get_param_fixed = addAllToGetParam();
            window.location.href = "../public/checkout.html" + get_param_fixed;
        });
    });
});

// Prints cart to console
function print_cart_to_console(){
    console.log(my_order);
}

//Thread loop for printing cart to console
setInterval(print_cart_to_console, 1000);