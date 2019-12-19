//----------------------------- Function Hide Menu on Scroll --------------------------------------------
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  // this.console.log("currentScrollPos : " + currentScrollPos);
  
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


//----------------------------- Function Promotion-image-slider --------------------------------------------------
var slideIndex_promotion_image_slider = 1;
promotion_slider_showSlides(slideIndex_promotion_image_slider);

function promotion_slider_plus_slides(n) {
  promotion_slider_showSlides(slideIndex_promotion_image_slider += n);
}

function promotion_slider_current_slides(n) {
  promotion_slider_showSlides(slideIndex_promotion_image_slider = n);
}

function promotion_slider_showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("image-promotion-slider");
  var dots = document.getElementsByClassName("promotion-slider-dot");
  if (n > slides.length) {slideIndex_promotion_image_slider = 1}    
  if (n < 1) {slideIndex_promotion_image_slider = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex_promotion_image_slider-1].style.display = "block";  
  dots[slideIndex_promotion_image_slider-1].className += " active";
}

//----------------------------- Function side-nav --------------------------------------------------
function openNav() {
  document.getElementById("sidenav").style.width = "250px";
  document.getElementById("filter-button").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
  document.getElementById("sidenav").style.width = "0";
  document.getElementById("filter-button").style.marginLeft = "0";
  document.body.style.backgroundColor = "white";
}




