/* ********************** ITEM-QUANTITY *************************** */

var item_quantity_value = 0;
function increase_Item_Quantity() {
    var item_quantity_value = parseInt(document.getElementsByClassName('number-item-quantity').item_quantity_value, 10);
    item_quantity_value = isNaN(item_quantity_value) ? 0 : item_quantity_value;
    item_quantity_value++;

    if(item_quantity_value >= 15){
        item_quantity_value = 15;
    }

    document.getElementsByClassName('number-item-quantity').item_quantity_value = item_quantity_value;
    document.getElementsByClassName('number-item-quantity')[0].value = item_quantity_value;
    document.getElementsByClassName('number-item-quantity')[1].value = item_quantity_value;

    console.log("CHECK : " + item_quantity_value);
}

function decrease_Item_Quantity() {
    var item_quantity_value = parseInt(document.getElementsByClassName('number-item-quantity').item_quantity_value, 10);
    item_quantity_value = isNaN(item_quantity_value) ? 0 : item_quantity_value;
    item_quantity_value < 1 ? item_quantity_value = 1 : '';
    item_quantity_value--;
    
    document.getElementsByClassName('number-item-quantity').item_quantity_value = item_quantity_value;
    document.getElementsByClassName('number-item-quantity')[0].value = item_quantity_value;
    document.getElementsByClassName('number-item-quantity')[1].value = item_quantity_value;

    console.log("CHECK : " + item_quantity_value);
}




  