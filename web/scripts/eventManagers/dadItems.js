
function dadItemsStart(e) {
    nameCell = e.path[0].cells[1];
    chooseItem(nameCell.id);

    copiedPaths = [];
    for (let i = 0; i < chosenItems.length; i++) {
        var item = document.getElementById(chosenItems[i]);
        
        var parent = findParent(item);
        var path = getPath(parent.getAttribute("id"));
        copiedPaths.push(path + "\\" + item.innerHTML);
    }
    e.dataTransfer.setData("text/plain", copiedPaths);
}

async function dadItemsDrop(e) {
    levitation = 0;
    var pastePath;

    copiedPaths = e.dataTransfer.getData("text/plain").split(",");
    var parent = findParent(e.target);
    var path = getPath(parent.getAttribute("id"));

    unChooseItems(null, true);

    e.target.classList.remove("dragOver");
    if (e.target.classList.contains("folder")) {
        pastePath = path + "\\" + e.target.innerHTML;
    }
    else {
        pastePath = path;
    }

    if (pastePath == getFolder(copiedPaths[0])) {
        return;
    }

    var endpoint = "move";

    if (!window.event.ctrlKey) {
        endpoint = "copy";
    }

    var response = await callEndpoint("POST", "/file/" + endpoint, prepareCopyRequest(pastePath));
    if (response.ERROR != null) {
        showWrongAlert("ERROR", response.ERROR, alertTime);
    }
    else {
        buildFolder(parent.id);
    }
}


function dadItemsEnter(e) {
    levitation = 0;
    e.preventDefault();
    if (e.target.classList.contains("folder"))
        e.target.classList.add("dragOver");
}

function dadItemsOver(e) {
    e.preventDefault();
    if (e.target.classList.contains("folder")) {
        levitation++;
        e.target.classList.add("dragOver");

        if (levitation >= 100) {
            levitation = 0;
            if (e.target.innerHTML != "..") {
                moveIn(e.target.innerHTML);
            }
            else {
                moveUp();
            }
        }
    } else {
        levitation = 0;
    }
}

function dadItemsLeave(e) {
    levitation = 0;
    e.target.classList.remove("dragOver");
}

function prepareCopyRequest(pastePath) {
    return {
        "PATH": pastePath,
        "ITEMS": copiedPaths
    }
}