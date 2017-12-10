var classNames = new Array()

// Filters
function setFilter(names) {
  var allPosts = document.getElementsByClassName("post")
  for (var i = 0; i < allPosts.length; i++) {
    var currentPost = allPosts[i]

  }
}

function activateFilter(name, id) {
  // First, we highlight and change the classNames thing (which is later used for the classification)
  var self = document.getElementById(id)
  if (contains.call(classNames, name)) { // If the classNames contains the inputted filter class name...
    // This section removes the className from classNames
    var index = classNames.indexOf(name) // APPARENTLY indexOf() DOESN'T WORK IN IE FUCK SOMEONE FIX THIS SHIT
    classNames.splice(index, 1)
    // Now we remove the highlighted class
    self.classList.remove("filter-chosen")
  } else {
    // This section adds the className to classNames (easier than removing it)
    classNames.push(name)
    // Now we add the highlighted class
    self.classList.add("filter-chosen")
  }

  // Now, the final piece, the classification
  // setFilter(classNames)

}

// This isn't mine (StackOverflow bruv), just use it to check if an array contains an element
var contains = function(needle) {
    // Per spec, the way to identify NaN is that it is not equal to itself
    var findNaN = needle !== needle;
    var indexOf;
    if(!findNaN && typeof Array.prototype.indexOf === 'function') {
        indexOf = Array.prototype.indexOf;
    } else {
        indexOf = function(needle) {
            var i = -1, index = -1;
            for(i = 0; i < this.length; i++) {
                var item = this[i];
                if((findNaN && item !== item) || item === needle) {
                    index = i;
                    break;
                }
            }
            return index;
        };
    }
    return indexOf.call(this, needle) > -1;
};
