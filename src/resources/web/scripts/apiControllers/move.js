function move(e, path) {
    var parent = findParent(e);
    
    if (changePath(parent.id, path)) {
        buildFolder(parent.id);
    }
    else {
        showWrongAlert("ERROR", "Error occurred :/", alertTime);
    }
}

function moveIn(e, folderName) {
    var parent = findParent(e);
    var path = getPath(parent.id);
    path += "\\" + folderName;
    
    if (changePath(parent.id, path)) {
        buildFolder(parent.id);
    }
    else {
        showWrongAlert("ERROR", "Error occurred :/", alertTime);
    }
}

function moveUp(e) {
    var parent = findParent(e);
    var path = getPath(parent.id);

    if (changePath(parent.id, getFolder(path))) {
        buildFolder(parent.id);
    }
    else {
        showWrongAlert("ERROR", "Error occurred :/", alertTime);
    }
}

function moveDirectFromTree(id) {
    var item = document.getElementById(id);
    var path = getTreePath(item);
    move(item, path);
}

function getFolder(fldr) {
    folderSplit = fldr.split("\\");
    fldr = "";
    for (let i = 0; i < folderSplit.length-1; i++) {
        fldr += folderSplit[i];
        if (i < folderSplit.length-2) {
            fldr += "\\";
        }
    }
    return fldr;
}