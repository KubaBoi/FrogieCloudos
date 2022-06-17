
function copyDirectory(e) {
    var parent = findParent(e);
    var path = getPath(parent.id);
    navigator.clipboard.writeText(path);
    showOkAlert("Copied :)", `${path} was saved in clipboard`, 1000);
}

var fcc = false;
function editPathDialog(e) {
    var parent = findParent(e);
    var label = parent.querySelector("#folderPathLabel");
    var path = label.innerHTML;
    if (path.startsWith("<")) return;
    label.innerHTML = "";

    var inp = createElement("input", label, "", 
    [
        {"name": "value", "value": path},
        {"name": "oninput", "value": "this.size = this.value.length"},
        {"name": "id", "value": "editPathInp"}
    ]);
    inp.setAttribute("size", inp.value.length);
    fcc = true;
}

function editPath(e) {
    try {
        var parent = findParent(e);
    }
    catch {
        return;
    }
    var label = parent.querySelector("#folderPathLabel");
    var editInp = parent.querySelector("#editPathInp");
    var path = label.innerHTML;
    
    if (e == editInp) return;
    if (fcc) {
        fcc = false;
        return;
    } 
    
    if (path.startsWith("<")) {
        path = editInp.value;
        if (path != "C:\\" && path.endsWith("\\")) {
            path = path.substring(0, path.length - 1);
        }
        else if (path == "C:") {
            path += "\\"
        }
        changePath(parent.id, path);
        buildFolder(parent.id);
    }
}

function chooseItem(id) {
    var item = document.getElementById(id);
    if (doesRenamingExists()) {
        if (isRenaming(item)) {
            return;
        } else {
            rename();
        }
    }

    for (let i = 0; i < chosenItems.length; i++) {
        if (chosenItems[i] == id) return;
    }
    item.classList.add("chosenItem");
    chosenItems.push(id);
}

function unChooseItems(element, overCrtl=false) {

    editPath(element);

    var floatingFileMenu = document.getElementById("fileMenuTable");
    floatingFileMenu.classList.remove("floatingMenuShow");

    if (window.event.ctrlKey && !overCrtl) return;
    
    for (let i = 0; i < chosenItems.length; i++) {
        var item = document.getElementById(chosenItems[i]);

        if (item == element || item == null) continue

        item.classList.remove("chosenItem");
        chosenItems.splice(i, 1);
        i--;
    }
}

function doesRenamingExists() {
    if (document.getElementById("renameInput") != null) {
        return true;
    }
    return false;
}

function isRenaming(item) {
    if (document.getElementById("renameInput").parentNode == item) {
        return true;
    }
    return false;
}

document.addEventListener("click", function (e) {
    unChooseItems(e.target);
});

// cancel browser menu
window.oncontextmenu = function (e)
{
    var elem = e.target;
    if (!elem.classList.contains("file") && 
        !elem.classList.contains("folder") &&
        !elem.classList.contains("contentDiv") ||
        elem.innerHTML == "..") 
        return;

    if (!elem.classList.contains("contentDiv")) {
        chooseItem(e.target.id);
    }
    if (!window.event.ctrlKey) unChooseItems(e.target);
    itemForFloatMenu = e.target;

    var r = document.querySelector(":root");

    var x = e.clientX;
    if (e.clientX >= document.body.scrollWidth - 200) x = e.clientX - 150;

    var y = e.clientY + 15;
    if (e.clientY >= document.body.scrollHeight - 300) y = e.clientY - 285;
    
    r.style.setProperty("--floatingMenuPositionX", x + "px");
    r.style.setProperty("--floatingMenuPositionY", y + "px");

    var floatingFileMenu = document.getElementById("fileMenuTable");
    floatingFileMenu.classList.add("floatingMenuShow");

    return false;
}