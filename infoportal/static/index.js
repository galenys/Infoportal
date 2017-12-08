// Catagories
function setCatagory(name) {
  var allImages = document.getElementsByClassName("item")
  for (var i = 0; i < allImages.length; i++) {
    if (allImages[i].classList.contains(name)) { //check if the image is part of the desired class
      allImages[i].style.display = "inline-block"
    } else {
      allImages[i].style.display = "none"
    }
  }
}
