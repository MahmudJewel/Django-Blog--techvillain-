console.log('Js connected !!!')

// Add active class to the current button (highlight it)

// let header = document.getElementById("navbarSupportedContent");
// let btns = header.getElementsByClassName("btn");
// for (let i = 0; i < btns.length; i++) {
//   btns[i].addEventListener("click", function () {
//     let current = document.getElementsByClassName("active");
//     current[0].className = current[0].className.replace(" active", "");
//     this.className += " active";
//     console.log(this.className)
//   });
// }


// responsive left-index 
const burger=document.querySelector(".burger");
const nav=document.querySelector(".nav_right");
const bb=document.querySelector(".bb");

 // for sliding navbar
burger.addEventListener('click', navSlide);  
bb.addEventListener('click', navSlide);

function navSlide(){
	nav.classList.toggle('nav_active');
	burger.classList.toggle('toggle');
}