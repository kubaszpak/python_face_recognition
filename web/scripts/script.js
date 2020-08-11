// function myFunction() {
//   var x = document.getElementById("wave-one");
//   if (x.style.display === "none") {
//     x.style.display = "block";
//   } else {
//     x.style.display = "none";
//   }
// }

function showFace(){
    eel.rec()(setImage);
}

function setImage(picture) {
  document.getElementById("face").src = "data:image/png;base64," + picture;
}

// function dummy(){
//   eel.dummy()(testFunc);
// }
// function testFunc(text){
//   document.getElementById("testP").innerHTML = text;
// }