
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

//----------------------------- Function Sidebar-menu's collapsible --------------------------------------------
var collapsible_sidebar_menu = document.getElementsByClassName("sidebar-collapsible-btn");
var collapsible_sidebar_menu_num;

for(collapsible_sidebar_menu_num = 0; collapsible_sidebar_menu_num < collapsible_sidebar_menu.length; collapsible_sidebar_menu_num ++){
  collapsible_sidebar_menu[collapsible_sidebar_menu_num].addEventListener("click", function() {
    this.classList.toggle("active");
    var collapsible_sidebar_menu_content = this.nextElementSibling;

    if(collapsible_sidebar_menu_content.style.maxHeight) {
      collapsible_sidebar_menu_content.style.maxHeight = null;
    } else {
      collapsible_sidebar_menu_content.style.maxHeight = collapsible_sidebar_menu_content.scrollHeight + "px";
    }
  })
}
//----------------------------- Function Sidebar-menu's Range slider --------------------------------------------
var left_price_slider = document.getElementById("left-price-slider-id");
var output_left_price_slider = document.getElementById("left-slider-value");
output_left_price_slider.innerHTML = left_price_slider.value;

left_price_slider.oninput = function() {
  output_left_price_slider.innerHTML = this.value;
}

// ------------------------------------ Modal ----------------------------------------
// Get the modal
var modal = document.getElementById("cart");

// Get the button that opens the modal
var btn = document.getElementById("showcart");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}