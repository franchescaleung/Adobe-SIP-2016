var slideIndex = 1;


window.onload=function(){
 //alert("Explore my world!");
 showSlides(slideIndex);
}


function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
}

// window.onload=function(){
//     document.addEventListener('click', changePhoto);
//  document.addEventListener('load', function(){
//      var div =document.getElementByClassName('pics1')[0];
// div.addEventListener('click', changePhoto);});
// // }

// // }    

// window.onload= function(){
//     changePhoto()
// }


// function changePhoto(event){
//     console.log('hello');
//     event.target.children[0].src= "https://m1.fluidreview.com/media/assets/reviewrooms/girlswhocode/logo/Girls-Who-Code-Summer-Program_821x234.png";
// }
    
//     //element.src=newPath;
// (pics1).hover(makeBigger, returntooriginal);
// function makeBigger(){
//     (this).css({height:'+=20%', width: '+=20%'});

// }

// function returntooriginal(){

//     (this).css({height:'+=20%', width: '+=20%'})
//}

// function rollover(my_image){
//     height= '+=20%', width= '+=20%'
// }

// function mouseaway(my_image){
//     height= '-=20%' width= '-=20%'
// }

// onmouseover="rollover(this)" 
// onmouseout="mouseaway(this)"