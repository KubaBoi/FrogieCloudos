var table = document.querySelector("#tableId");
var allData = "";
var jsonData = "";
var iconSize = 30;

function getFiles() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(this.responseText);
            allData = jsonData;
            
            sort();
            
            table.innerHTML = "";
            addHeadRow();
            for (var i = 0; i < jsonData.length; i++) {
                addRow(jsonData[i]);
            } 
        }
    };
    xhttp.open("GET", "/getFiles", true);
    xhttp.send();
}

function addRow(data) {
    var name = data.filename;
    var size = data.size;
    var type = data.type;
    var date = formatDate(data.date);

    var row = document.createElement("tr");

    var cellIcon = document.createElement("td");
    var cellName = document.createElement("td");
    var cellDate = document.createElement("td");
    var cellSize = document.createElement("td");
    var cellDownload = document.createElement("td");
    var cellRemove = document.createElement("td");

    cellIcon.innerHTML = "<img src=\"/images/" + type + "Icon.png\" alt=\"typeIcon\" width=" + iconSize + " heigth=" + iconSize +">";
    cellName.innerHTML = "<a href=\"/files/" + name + "\" target=\"_blank\">" + name + "</a>";
    cellDate.innerHTML = date;
    cellSize.innerHTML = size;
    cellDownload.innerHTML = "<a href=\"/files/" + name + "\" download=\"" + name + "\"><img src=\"/images/downloadIcon.png\" alt=\"downloadIcon\" width=" + iconSize + " heigth=" + iconSize +"></a>";
    cellRemove.innerHTML = "<img src=\"/images/removeIcon.png\" onclick=\"removeFile('" + name + "')\" alt=\"removeIcon\" width=" + iconSize + " heigth=" + iconSize +">";

    cellIcon.setAttribute("style", "width: 1%");
    cellDownload.setAttribute("style", "width: 1%;");
    cellRemove.setAttribute("style", "width: 1%;");

    row.appendChild(cellIcon);
    row.appendChild(cellName);
    row.appendChild(cellDate);
    row.appendChild(cellSize);
    row.appendChild(cellDownload);
    row.appendChild(cellRemove);

    table.appendChild(row);
}

function formatDate(unixTime) {
    var date = new Date(unixTime * 1000);

    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hours = "0" + date.getHours();
    var minutes = "0" + date.getMinutes();

    return  day + "." + month + "." + year + " " + hours.substr(-2) + ':' + minutes.substr(-2);
}

function addHeadRow() {
    var row = document.createElement("tr");

    var cellIcon = document.createElement("th");
    var cellName = document.createElement("th");
    var cellDate = document.createElement("th");
    var cellSize = document.createElement("th");

    cellName.innerHTML = "Název/Zobrazit soubor";
    cellDate.innerHTML = "Čas uploadu";
    cellSize.innerHTML = "Velikost";

    row.appendChild(cellIcon);
    row.appendChild(cellName);
    row.appendChild(cellDate);
    row.appendChild(cellSize);

    table.appendChild(row);
}

function noFiles() {
    var row = document.createElement("tr");

    var cellName = document.createElement("td");

    cellName.innerHTML = "<img src=\"/images/sadFrog.png\" alt=\"typeIcon\"> Nenašel jsem žádné soubory :(";

    row.appendChild(cellName);

    table.appendChild(row);
}