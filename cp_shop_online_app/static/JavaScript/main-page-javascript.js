//----------------------------- Function Promotion's slideshow --------------------------------------------
var slideIndex_promotion = 1;
var myIndex_promotion = 0;
carousel_promotion();
showSlides_promotion(slideIndex_promotion);

function plusSlides_promotion(n) {
  showSlides_promotion((slideIndex_promotion += n));
}

function currentSlide_promotion(n) {
  showSlides_promotion((slideIndex_promotion = n));
}

function showSlides_promotion(n) {
  var i;
  var slides = document.getElementsByClassName("slides-promotion");
  var dots = document.getElementsByClassName("dot");


  if (n > slides.length) {
    slideIndex_promotion = 1;
  }
  if (n < 1) {
    slideIndex_promotion = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex_promotion - 1].style.display = "block";
  dots[slideIndex_promotion - 1].className += " active";
}

function carousel_promotion() {
  var i;
  var x = document.getElementsByClassName("slides-promotion");

  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  myIndex_promotion++;
  if (myIndex_promotion > x.length) {
    myIndex_promotion = 1;
  }

  currentSlide_promotion(myIndex_promotion);

  if(myIndex_promotion !== 0 ){
      
  }
  
  x[myIndex_promotion - 1].style.display = "block";  
  setTimeout(carousel_promotion, 3000);
}

//----------------------------- Function Advertisment's slideshow --------------------------------------------
var slideIndex_slideshow_container_advertisement = [1, 1];
var slideId_advertisment = ["mySlides_slideshow_advertisement"];
var myIndex_slideshow_advertisment = 0;
carousel_advertisment();
slideshow_advertisement(1, 0);
slideshow_advertisement(1, 1);
function plusSlides_slideshow_container_advertisement(n, no) {
  slideshow_advertisement(
    (slideIndex_slideshow_container_advertisement[no] += n),
    no
  );
}
function slideshow_advertisement(n, no) {
  var i;
  var x = document.getElementsByClassName(slideId_advertisment[no]);
  if (n > x.length) {
    slideIndex_slideshow_container_advertisement[no] = 1;
  }
  if (n < 1) {
    slideIndex_slideshow_container_advertisement[no] = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }

  if (no !== 1) {
    x[slideIndex_slideshow_container_advertisement[no] - 1].style.display = "block";
  }
}
function carousel_advertisment() {
  var i;
  var x = document.getElementsByClassName("mySlides_slideshow_advertisement");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  myIndex_slideshow_advertisment ++;
  if (myIndex_slideshow_advertisment > x.length) {
    myIndex_slideshow_advertisment = 1;
  }

  console.log("MY Index : " + myIndex_slideshow_advertisment);

  x[myIndex_slideshow_advertisment - 1].style.display = "block";
  setTimeout(carousel_advertisment, 3000);
}



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
