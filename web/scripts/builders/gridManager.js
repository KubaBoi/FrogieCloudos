
var gridStyle = 0;
var gridStyles = [
    [ // normal
        ["100%", "100%", '"win1"'],
        ["50% 50%", "100%", '"win1 win2"'],
        ["50% 50%", "50% 50%", '"win1 win2" "win3 win3"'],
        ["50% 50%", "50% 50%", '"win1 win2" "win3 win4"'],
        ["33% 33% 33%", "50% 50%", '"win1 win1 win2" "win3 win4 win5"'],
        ["33% 33% 33%", "50% 50%", '"win1 win2 win3" "win4 win5 win6"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win1 win2 win3" "win4 win5 win6 win7"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win2 win3 win4" "win5 win6 win7 win8"']
    ],
    [ // top
        ["100%", "100%", '"win1"'],
        ["100%", "50% 50%", '"win1" "win2"'],
        ["50% 50%", "50% 50%", '"win1 win1" "win2 win3"'],
        ["33% 33% 33%", "50% 50%", '"win1 win1 win1" "win2 win3 win4"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win1 win1 win1" "win2 win3 win4 win5"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win1 win1 win2" "win3 win4 win5 win6"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win1 win2 win3" "win4 win5 win6 win7"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win2 win3 win4" "win5 win6 win7 win8"']
    ],
    [ // right
        ["100%", "100%", '"win1"'],
        ["50% 50%", "100%", '"win2 win1"'],
        ["50% 50%", "50% 50%", '"win2 win1" "win3 win1"'],
        ["50% 50%", "33% 33% 33%", '"win2 win1" "win3 win1" "win4 win1"'],
        ["33% 33% 33%", "50% 50%", '"win2 win3 win1" "win4 win5 win1"'],
        ["33% 33% 33%", "33% 33% 33%", '"win2 win2 win1" "win3 win4 win1" "win5 win6 win1"'],
        ["25% 25% 25% 25%", "50% 50%", '"win2 win3 win4 win1" "win5 win6 win7 win1"'],
        ["25% 25% 25% 25%", "50% 50%", '"win2 win3 win4 win1" "win5 win6 win7 win8"']
    ],
    [ // left
        ["100%", "100%", '"win1"'],
        ["50% 50%", "100%", '"win1 win2"'],
        ["50% 50%", "50% 50%", '"win1 win2" "win1 win3"'],
        ["50% 50%", "33% 33% 33%", '"win1 win2" "win1 win3" "win1 win4"'],
        ["33% 33% 33%", "50% 50%", '"win1 win2 win3" "win1 win4 win5"'],
        ["33% 33% 33%", "33% 33% 33%", '"win1 win2 win2" "win1 win3 win4" "win1 win5 win6"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win2 win3 win4" "win1 win5 win6 win7"'],
        ["25% 25% 25% 25%", "50% 50%", '"win1 win2 win3 win4" "win5 win6 win7 win8"']
    ]
]

function setGridStyle(imgId) {    
    setCookie("gridType", imgId, 300);

    var gridStylesImgs = document.body.getElementsByClassName("clickableImg");
    for (var i = 0; i < gridStylesImgs.length; i++) {
        var item = gridStylesImgs[i];
        item.classList.remove("chosenGridStyle");
    }
    var img = document.getElementById(imgId);
    img.classList.add("chosenGridStyle");
    gridStyle = img.getAttribute("value");

    doGrid();
}

function doGrid() {
    setFoldersCookies();
    switch (folders.length) {
        case 1: 
            changeGrid();
            break;
        case 2:
            changeGrid();
            break;
        case 3:
            changeGrid();
            break;
        case 4:
            changeGrid();
            break;
        case 5:
            changeGrid();
            break;
        case 6:
            changeGrid();
            break;
        case 7:
            changeGrid();
            break;
        case 8:
            changeGrid();
            break;
    }
}

function changeGrid() {
    var openFoldersDiv = document.getElementById("windowsDiv");

    openFoldersDiv.style.gridTemplateColumns = gridStyles[gridStyle][folders.length-1][0];
    openFoldersDiv.style.gridTemplateRows = gridStyles[gridStyle][folders.length-1][1];
    openFoldersDiv.style.gridTemplateAreas = gridStyles[gridStyle][folders.length-1][2];
}