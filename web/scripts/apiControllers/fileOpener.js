async function openFile(e, file) {
    var parent = findParent(e);
    var path = getPath(parent.id);

    var response = await callEndpoint("GET", `/main/open?path=${path}\\${file}`);
    if (response.ERROR != null) {
        showWrongAlert("ERROR", response.ERROR, alertTime);
    }
}

function getTreePath(e) {
    var parent = e.parentNode;
    var pathArray = [];
    
    while (!parent.id.startsWith("treeTable")) {
        if (parent.nodeName != "UL") {
            childSpan = parent.childNodes[0];
            pathArray.push(childSpan.getAttribute("value"));
        }
        parent = parent.parentNode;
    }
    var path = pathArray.reverse().join("\\");
    return getRoot(parent.parentNode.parentNode.parentNode.id) + path;
}

async function openCmd(e) {
    var parent = findParent(e);
    var path = getPath(parent.id);

    var response = await callEndpoint("GET", `/main/cmd?path=${path}`);
    if (response.ERROR != null) {
        showWrongAlert("ERROR", response.ERROR, alertTime);
    }
}

async function openCode(e) {
    var parent = findParent(e);
    var path = getPath(parent.id);

    var response = await callEndpoint("GET", `/main/code?path=${path}`);
    if (response.ERROR != null) {
        showWrongAlert("ERROR", response.ERROR, alertTime);
    }
}