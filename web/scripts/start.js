var folders = [];
var chosenItems = [];
var copiedPaths = [];
var debug = true;

var alertTime = 3000;

var startArray = [
    "menu",
    "fileMenu"
];

var renameDialogParent = null;
var renameDialogTd = null;
var fileNameOriginal = "";

var itemForFloatMenu = null;

var resizeDefX = null;
var parentTree = null;

async function start() {
    var response = await callEndpoint("GET", "/main/init");
    if (response.ERROR == null) {
        openFolder(response.PATH, response.ROOT);
    }
    else {
        showWrongAlert("ERROR", response.ERROR, alertTime);
    }
}

loadPage(startArray, function() {start();});