// this is an async timeout util
const timeout = async (ms) => new Promise((res) => setTimeout(res, ms));

let next = false; // this is to be changed on user input

async function waitUserInput() {
  while (next === false) await timeout(50); // pause script but avoid browser to freeze ;)
  const userInputVal = next;
  next = false; // reset var
  return userInputVal;
}

function button1Clicked() {
  next = "yes";
}

function button2Clicked() {
  next = "no";
}

function py_video() {
  eel.video_feed()();
}

eel.expose(updateImageSrc);
function updateImageSrc(val) {
  let elem = document.getElementById("face");
  elem.src = "data:image/jpeg;base64," + val;
}

eel.expose(changeDisplay);
function changeDisplay(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  return factor();
}

async function factor(){
  // const userResponse = await waitUserInput();
  return "yes";
}

document.addEventListener("DOMContentLoaded", function () {
  py_video();
});
