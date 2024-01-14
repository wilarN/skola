// Import all menu items from order.js

import { menuItems } from './menu.js';


function getOrderFromGetParams() {
    let getParams = window.location.search;
    let getParamsArray = getParams.split("&");
    if (getParamsArray.length > 0) {
        // Remove first ? from element at index 0.
        getParamsArray[0] = getParamsArray[0].slice(1);
    }

    let orderArray = [];
    getParamsArray.forEach(item => {
        orderArray.push(menuItems.find(menuItem => menuItem.id === parseInt(item, 10)));
    });
    return orderArray;
}

function displayOrder() {
    const my_order = getOrderFromGetParams();
    const orderContainer = document.querySelector("#order-container");
    const totalContainer = document.querySelector("#total-container");
    let total = 0;

    if (my_order.length > 0) {
        my_order.forEach(item => {
            const orderItem = document.createElement("div");
            orderItem.classList.add("order-item");

            // Check if the item is not undefined before accessing its properties
            if (item) {
                const orderImg = document.createElement("img");
                orderImg.classList.add("order-img");
                orderImg.src = item.img;
                orderItem.appendChild(orderImg);

                const orderName = document.createElement("p");
                orderName.classList.add("order-name");
                orderName.innerText = item.name;

                const orderPrice = document.createElement("p");
                orderPrice.classList.add("order-price");
                orderPrice.innerText = item.price + " kr";

                orderItem.appendChild(orderName);
                orderItem.appendChild(orderPrice);
                orderContainer.appendChild(orderItem);
                total += item.price;

                const spacer = document.createElement("div");
                spacer.classList.add("spacer");
                orderContainer.appendChild(spacer);

                const removeButton = document.createElement("button");
                removeButton.classList.add("remove-button");
                removeButton.innerText = "X";
                removeButton.addEventListener("click", () => {
                    removeCartItem(item.id);
                });

                orderItem.appendChild(removeButton);
            }
        });
    } else {
        const noItems = document.createElement("p");
        noItems.classList.add("no-items");
        noItems.innerText = "No items in order";
        orderContainer.appendChild(noItems);
    }
    
    // display total price
    // #topay
    document.getElementById("topay").innerText = "To Pay: "+total + " kr";    

}


function removeCartItem(itemID) {
    // remove item with id from get parameters
    const my_order = getOrderFromGetParams();
    const item = my_order.find(item => item.id === itemID);
    if (item) {
        my_order.splice(my_order.indexOf(item), 1);
        // Reload page with new get parameters
        let getParam = "?";
        my_order.forEach(item => {
            getParam += item.id + "&";
        });
        getParam = getParam.slice(0, -1);
        window.location.href = "checkout.html" + getParam;
    }
}


displayOrder();