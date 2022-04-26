function findByParent(type, argument, parent) {
    var allElements = [];
    if (type == "class") allElements = document.body.getElementsByClassName(argument);
    else if (type == "tag") allElements = document.body.getElementsByTagName(argument);

    for (var i = 0; i < allElements.length; i++) {
        var testedParent = findParent(allElements[i]);
        if (testedParent == parent) {
            return allElements[i];
        }
    }
}