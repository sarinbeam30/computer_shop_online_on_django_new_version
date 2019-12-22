
//----------------------------- Function Hide Menu on Scroll --------------------------------------------
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  
  if(currentScrollPos === 0){
    document.getElementById("panel-header-hide-menu-on-scroll").style.top = "0";
    document.getElementById("header-sticky").style.marginTop = "30px";
  }

  else{
    document.getElementById("panel-header-hide-menu-on-scroll").style.top = "-30px";
    document.getElementById("header-sticky").style.marginTop = "0";
  }

  prevScrollpos = currentScrollPos;
}

//----------------------------- Function Footer's collapsible --------------------------------------------
var collapsible_footer = document.getElementsByClassName("footer-collapsible-button");
var collapsible_footer_n;

for(collapsible_footer_n = 0; collapsible_footer_n < collapsible_footer.length; collapsible_footer_n ++){
  collapsible_footer[collapsible_footer_n].addEventListener("click", function() {
    this.classList.toggle("active");
    var collapsible_footer_content = this.nextElementSibling;

    if(collapsible_footer_content.style.maxHeight) {
      collapsible_footer_content.style.maxHeight = null;
    } else {
      collapsible_footer_content.style.maxHeight = collapsible_footer_content.scrollHeight + "px";
    }
  });
}

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
    

    console.log("CHECK : " + item_quantity_value);
}

function decrease_Item_Quantity() {
    var item_quantity_value = parseInt(document.getElementsByClassName('number-item-quantity').item_quantity_value, 10);
    item_quantity_value = isNaN(item_quantity_value) ? 0 : item_quantity_value;
    item_quantity_value < 1 ? item_quantity_value = 1 : '';
    item_quantity_value--;
    
    document.getElementsByClassName('number-item-quantity').item_quantity_value = item_quantity_value;
    document.getElementsByClassName('number-item-quantity')[0].value = item_quantity_value;
    

    console.log("CHECK : " + item_quantity_value);
}
