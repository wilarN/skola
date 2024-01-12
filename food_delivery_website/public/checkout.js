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

    if(my_order.length > 0){
        const ul = document.createElement('ul');
        my_order.forEach(item => {
            const li = document.createElement('li');
            const div = document.createElement('div');
        });
    } else {
        orderContainer.textContent = 'Your order is empty.';
    }
}

displayOrder();