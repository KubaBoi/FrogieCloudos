
function dadSizerStart(e) {
    parentTree = findParent(e.target);
    parentTree = findByParent("class", "treeDiv", parentTree);

    resizeDefX = e.clientX - parseInt(getComputedStyle(parentTree).getPropertyValue("width").replace("px", ""));
}

function dadSizerEnter(e) {
    parentTree.style.width = (e.clientX - resizeDefX) + "px";
}

function dadSizerOver(e) {
    parentTree.style.width = (e.clientX - resizeDefX) + "px";
}

function dadSizerLeave(e) {
    parentTree.style.width = (e.clientX - resizeDefX) + "px";
}

function dadSizerDrop(e) {
    resizeDefX = null;
}