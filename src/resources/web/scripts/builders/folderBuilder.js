
async function buildFolder(divId) {
    var parentDiv = document.getElementById(divId);
    var folderTable = parentDiv.querySelector("#folderTable");

    var folder = getPath(divId);
    parentDiv.querySelector("#folderPathLabel").innerHTML = folder;

    clearTable(folderTable);
    chosenItems = [];

    var response = await callEndpoint("GET", `/main/ls?path=${folder}`);
    if (response.ERROR == null) {
        var folderItems = response.FOLDER;
        
        if (folderItems.length == 0) {
            var response2 = await callEndpoint("GET", `/main/exists?path=${folder}`)
            if (response2.ERROR == null) {
                if (!response2.EXISTS) {
                    showWrongAlert("Not found", "Folder was not found", alertTime);
                    folderTable.innerHTML = "Folder was not found";
                    return;
                }
            } 
        }

        addHeader(folderTable, [
            {"text": "", "attributes":[]},
            {"text": "Name", "attributes":[]},
            {"text": "Size", "attributes":[]}
        ],[]);

        for (let i = 0; i < folderItems.length; i++) {
            var item = folderItems[i];

            var ondblclick = "moveIn(this, '" + item.NAME + "')";

            if (item.TYPE == "FILE") {
                ondblclick = "openFile(this, '" + item.NAME + "')";
            }

            var id = i;
            while (document.getElementById("row" + id) != null) id++;

            addRow(folderTable, [
                {"text": "<img src='images/" + item.IMAGE + "'>", "attributes": [
                    {"name": "class", "value": "iconCell"}
                ]},
                {"text": item.NAME, "attributes": [
                    {"name": "class", "value": item.TYPE.toLowerCase()},
                    {"name": "id", "value": "row" + id}
                ]},
                {"text": item.SIZE, "attributes": [
                    {"name": "class", "value": "sizeCell"}
                ]}
            ],
            [
                {"name": "ondblclick", "value": ondblclick},
                {"name": "onclick", "value": "chooseItem('row" + id + "')"},
                {"name": "draggable", "value": "true"}
            ]);
        }
    }
    else {
        showWrongAlert("ERROR", response.ERROR, alertTime);
    }
    setFoldersCookies();
}

function setFoldersCookies() {
    var foldersString = "";
    for (var i = 0; i < folders.length; i++) {
        foldersString += folders[i].PATH + "|" + folders[i].ROOT + ",";
    }
    foldersString = foldersString.substring(0, foldersString.length - 1);
    setCookie("openFolders", foldersString, 300);
}