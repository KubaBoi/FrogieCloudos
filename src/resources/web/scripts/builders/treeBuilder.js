
async function buildTree(divId) {
    var parentDiv = document.getElementById(divId);
    var treeTable = parentDiv.querySelector("#treeTable");

    clearTable(treeTable);
    chosenItems = [];

    var response = await callEndpoint("GET", `/main/ls?path=${getRoot(divId)}`);
    if (response.ERROR == null) {
        var treeItems = response.FOLDER;

        createLis(treeTable, treeItems);
    }
    else {
        showWrongAlert("ERROR", response.ERROR, alertTime);
    }
}

async function buildBranch(e) {
    var parent = e.parentNode;

    var childNodes = parent.childNodes;
    if (childNodes.length > 1) {
        for (var i = 0; i < childNodes.length; i++) {
            var node = childNodes[i];
            if (node.nodeName == "SPAN") continue;
            node.remove();
        }
        return;
    }

    var path = getTreePath(e);
    var response = await callEndpoint("GET", `/main/ls?path=${path}`);
    if (response.ERROR == null) {
        var newUL = createElement("ul", parent);
        var treeItems = response.FOLDER;

        createLis(newUL, treeItems);
    }
}

function createLis(parentUL, treeItems) {
    for (let i = 0; i < treeItems.length; i++) {
        var item = treeItems[i];

        if (item.TYPE == "FILE") continue;

        var id = 0;
        while (document.getElementById("treeRow" + id) != null) id++;

        var newLI = createElement("li", parentUL, "",
            [
                {"name": "id", "value": "treeRow" + id}
            ]
        );

        createElement("span", newLI, stringShorter(item.NAME, 15),
            [
                {"name": "ondblclick", "value": `buildBranch(this)`},
                {"name": "onclick", "value": `sglC(function(){moveDirectFromTree("${"treeSpan" + id}");})`},
                {"name": "id", "value": "treeSpan" + id},
                {"name": "value", "value": item.NAME},
                {"name": "title", "value": item.NAME}
            ]
        );
    }
}