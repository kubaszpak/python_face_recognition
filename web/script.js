function py_video() {
  eel.video_feed()();
}

eel.expose(updateImageSrc);
function updateImageSrc(val) {
  let elem = document.getElementById("face");
  elem.src = "data:image/jpeg;base64," + val;
}
