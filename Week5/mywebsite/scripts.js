window.onload=function(){
    document.addEventListener('click', changePhoto);
 document.addEventListener('load', function(){
     var div =document.getElementByClassName('pics1')[0];
div.addEventListener('click', changePhoto);});
// }

// }    

window.onload= function(){
    changePhoto()
}


function changePhoto(event){
    console.log('hello');
    event.target.children[0].src= "https://m1.fluidreview.com/media/assets/reviewrooms/girlswhocode/logo/Girls-Who-Code-Summer-Program_821x234.png";
}
    
    //element.src=newPath;
