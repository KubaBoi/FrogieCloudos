var sorted = document.querySelector("#sorted");
var asc = document.querySelector("#asc");

function sort() {
    if (sorted.value == "name") {
        jsonData = sortByName(jsonData, asc.value);
    }
    else if (sorted.value == "time") {
        jsonData = sortByTime(jsonData, asc.value);
    }
    else if (sorted.value == "size") {
        jsonData = sortbySize(jsonData, asc.value); 
    }
    else {
        jsonData = sortByType(jsonData, asc.value); 
    }

    table.innerHTML = "";
    if (jsonData.length == 0) {
        noFiles();
    }
    else {
        addHeadRow();
    }
    for (var i = 0; i < jsonData.length; i++) {
        addRow(jsonData[i]);
    } 
}

function sortByName(files, direction) {
    for (var i = 0; i < files.length - 1; i++) {
        for (var j = 0; j < files.length - i - 1; j++) {
            if (('' + files[j].filename).localeCompare(files[j+1].filename) == direction) {
                var tmp = files[j];
                files[j] = files[j+1];
                files[j+1] = tmp;
            }
        }
    } 
    return files;
}

function sortByType(files, direction) {
    for (var i = 0; i < files.length - 1; i++) {
        for (var j = 0; j < files.length - i - 1; j++) {
            if (('' + files[j].type).localeCompare(files[j+1].type) == direction) {
                var tmp = files[j];
                files[j] = files[j+1];
                files[j+1] = tmp;
            }
        }
    } 
    return files;
}

function sortByTime(files, direction) {
    for (var i = 0; i < files.length - 1; i++) {
        for (var j = 0; j < files.length - i - 1; j++) {
            if (direction == -1) {
                if (files[j].date > files[j+1].date) {
                    var tmp = files[j];
                    files[j] = files[j+1];
                    files[j+1] = tmp;
                }
            }
            else {
                if (files[j].date < files[j+1].date) {
                    var tmp = files[j];
                    files[j] = files[j+1];
                    files[j+1] = tmp;
                }
            }
        }
    } 
    return files;
}

function sortbySize(files, direction) {
    for (var i = 0; i < files.length - 1; i++) {
        for (var j = 0; j < files.length - i - 1; j++) {
            if (direction == -1) {
                if (files[j].byteSize > files[j+1].byteSize) {
                    var tmp = files[j];
                    files[j] = files[j+1];
                    files[j+1] = tmp;
                }
            }
            else {
                if (files[j].byteSize < files[j+1].byteSize) {
                    var tmp = files[j];
                    files[j] = files[j+1];
                    files[j+1] = tmp;
                }
            }
        }
    } 
    return files;
}