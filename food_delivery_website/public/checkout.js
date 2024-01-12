// Import all menu items from order.js

import { menuItems } from './menu.js';


function getOrderFromGetParams(){
    let getParams = window.location.search;
    let getParamsArray = getParams.split("&");
    if(getParamsArray.length > 0){
        // Remove first ? from element at index 0.
        getParamsArray[0] = getParamsArray[0].slice(1);
    }

    let orderArray = [];
    getParamsArray.forEach(item => {
        orderArray.push(menuItems.find(menuItem => menuItem.id === parseInt(item, 10)));
    });
    return orderArray;
}

function displayOrder(){
    const my_order = getOrderFromGetParams();
    const orderContainer = document.querySelector("#order-container");
    const totalContainer = document.querySelector("#total-container");
    let total = 0;
    my_order.forEach(item => {
        const orderItem = document.createElement("div");
        orderItem.classList.add("order-item");
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
        // Create spacer between order items to space them out
        const spacer = document.createElement("div");
        spacer.classList.add("spacer");
        orderContainer.appendChild(spacer);
    });
}

displayOrder();