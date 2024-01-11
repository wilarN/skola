
function getOrderFromGetParams(){
    let getParams = window.location.search;
    let getParamsArray = getParams.split("&");
    let orderArray = [];
    if(orderArray.length > 0){
        // Remove first ? from element at index 0.
        getParamsArray[0] = getParamsArray[0].slice(1);
    }

    console.log(getParamsArray);
}

getOrderFromGetParams();