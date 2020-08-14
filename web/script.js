// this is an async timeout util
const timeout = async (ms) => new Promise((res) => setTimeout(res, ms));

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

eel.expose(startTransmision);
function startTransmision() {
  eel.video_feed()();
}

let yesWasChosen = false;
let noWasChosen = false;

function clickedYes() {
  yesWasChosen = true;
}

function clickedNo() {
  noWasChosen = true;
}

eel.expose(updateImageSrc);
function updateImageSrc(val) {
  let elem = document.getElementById('face');
  elem.src = 'data:image/jpeg;base64,' + val;
}

eel.expose(changeDisplay);
function changeDisplay() {
  // var response;
  var x = document.getElementById('wave-one');
  if (x.style.display === 'none') {
    console.log('It was none till now');
    x.style.display = 'block';
  } else {
    console.log('It was not none till now');
    x.style.display = 'none';
  }
}

eel.expose(dealWithButtons);
function dealWithButtons() {
  loopUntilUserChooses();
  return 1;
}

function dealWithReturn() {
    if (yesWasChosen) {
      return true;
    } else if (noWasChosen) {
      return false;
    } else {
      return 'error';
    }
}

async function help() {
  await loopUntilUserChooses();
}

function loopUntilUserChooses() {
  if (yesWasChosen === false && noWasChosen === false) {
    // await sleep(500);
    console.log('It is working')
    setTimeout(loopUntilUserChooses , 200);
  }
}

// eel.expose(dealWithButtons2);
// function dealWithButtons2(){
//   while (yesWasChosen === false && noWasChosen === false) {
//     return Promise.resolve(sleep(500)).then(() => undefined);
//   }
//   if (yesWasChosen) {
//     return Promise.resolve(true);
//   } else if (noWasChosen) {
//     return Promise.resolve(false);
//   } else {
//     return Promise.resolve('error')
//   }
// }

// const pleaseClick1 = new Promise((resolve) => {
//   if (yesWasChosen) {
//     resolve("yes");
//   }
// });

// const pleaseClick2 = new Promise((resolve) => {
//   if (noWasChosen = false;) {
//     resolve("no");
//   }
// });

// Promise.race([pleaseClick1, pleaseClick2]).then((message) => {
//   console.log(message);
// });

// function testFunction() {
//   secondFunction();
// }

// document.addEventListener("DOMContentLoaded", function () {
//   eel.video_feed()();
// });

// function sleep(ms) {
//   return new Promise((resolve) => setTimeout(resolve, ms));
// }

// // eel.expose(secondFunction);
// const secondFunction = async () => {
//   const result = await dealWithButtons();
//   // do something else here after firstFunction completes
//   // return result;
//   console.log(result);
// };

// let next = "nothing"; // this is to be changed on user input
// let n = 0;

// async function waitUserInput() {
//   while (next === "nothing") await timeout(50); // pause script but avoid browser to freeze ;)
//   const userInputVal = next;
//   next = false; // reset var
//   return userInputVal;
// }
// while(true){
//   if(yesWasChosen == false && noWasChosen = false; == false){
//     continue;
//   }else if(yesWasChosen == true){
//     response = "yes";
//     break;
//   }
//   else if(noWasChosen = false; == true){
//     response = "no";
//     break;
//   }
// }
// return reponse;
// return factor2();
// console.log(dealWithButtons());
// return dealWithButtons();
// }

// async function factor(){
//   const userResponse = await waitUserInput();
//   return userResponse;
// }

// async function factor2() {
//   const userResponse = await dealWithButtons();
//   return userResponse;
// }

// <!-- <form class = buttons>
// <input type="radio" value="yes" class="button1">
// <img src="./icons/check-black-18dp.svg" alt="yes" class="checkmark">
// <input type="radio" value="no" class="button2">
// <img src="./icons/clear-black-18dp.svg" alt="no" class="wrong">
// </label>
// </form> -->
