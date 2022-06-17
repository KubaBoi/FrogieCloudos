
function dragStart(e) {
    if (e.target.nodeName == "DIV") {
        console.log(e.target);
        dadSizerStart(e);
    }
    else {
        dadItemsStart(e);
    }
}


function dragEnter(e) {
    if (resizeDefX != null) {
        dadSizerEnter(e);
    }
    else {
        dadItemsEnter(e);
    }
}

var levitation = 0;
function dragOver(e) {
    if (resizeDefX != null) {
        dadSizerOver(e);
    }
    else {
        dadItemsOver(e);
    }
}

function dragLeave(e) {
    if (resizeDefX != null) {
        dadSizerLeave(e);
    }
    else {
        dadItemsLeave(e);
    }
}

function drop(e) {
    if (resizeDefX != null) {
        dadSizerDrop(e);
    }
    else {
        dadItemsDrop(e);
    }
}

document.addEventListener("dragstart", dragStart);

document.addEventListener("dragover", dragOver);
document.addEventListener("dragleave", dragLeave);
document.addEventListener("dragenter", dragEnter);
document.addEventListener("drop", drop);
