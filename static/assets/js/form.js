let age =prompt("Enter Age");
let btn= document.querySelector(".button");
if(age<18){
    btn.classList.add("hide");
}