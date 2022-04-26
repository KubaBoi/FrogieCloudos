function apiFunction(url) {    
    return new Promise(resolve => {
        sendGet(url, debug, function(response){
            resolve(response);
        });  
    });
}

function restart() {
    if (confirm("Do you really want to restart your application?\nIt will took about 20 seconds.")) {
        clearInterval(updateInterval);
        document.getElementById("restartButt").disabled = true;
        apiFunction("/admin/restart");
        textInterval = setInterval(function() { loadingText("Waiting for response from server"); }, 200);
        setTimeout(buildTableWithDelay, 500);
    }
}

async function buildTableWithDelay() {
    response = await getActiveLog();
    if (!response.ERROR) {
        if (response.RESPONSE.LOG.includes("<label class='warning'>Restart will start in 5 seconds</label></td></tr>\n")) {
            clearInterval(textInterval);

            element = document.getElementById("log");
            var b = element.scrollHeight - element.clientHeight;
            element.scrollTop = b;
            
            prepareRestart();
            setTimeout(checkLife, 15000);
        }
        else {
            setTimeout(buildTableWithDelay, 500);
        }
    }
}

function prepareRestart() {
    textInterval = setInterval(function() { loadingText("Server is restarting"); }, 200);
}
var dots = 0;
function loadingText(text) {
    for (let i = 0; i < dots; i++) {
        text += ".";
    }
    dots += 1;
    if (dots >= 10) dots = 0;
    document.querySelector("#logTable").innerHTML = text;
}

async function saveChanges() {
    var configString = "{";
    var confTable = document.getElementById("settingsTable");
    var rows = confTable.querySelectorAll("tr");
    
    for (var i = 0; i < rows.length; i++) {
        var tds = rows[i].querySelectorAll("td");
        var inp = tds[1].querySelector("input");
        var val = validateValue(inp.value);
        configString += `"${tds[0].innerHTML}": ${val},`; 
    }
    configString = configString.substring(0, configString.length - 1);
    configString += "}";

    setCookie("config", configString, 0.01)
    var response = await callEndpoint("GET", "/admin/changeConfiguration");
    if (response.ERROR != null) {
        alert("ERROR: " + response.ERROR);
    }

}

function validateValue(value) {
    var int = parseInt(value);
    if (!isNaN(int) && int.toString().length == value.length) return int;
    else if (value == "false") return false;
    else if (value == "true") return true;
    return `"${value}"`;
}

async function checkLife() {
    fetch("/alive")
    .then(
        (response) => {
            updateInterval = setInterval(update, 1000);
            clearInterval(textInterval);
            document.getElementById("restartButt").disabled = false;
            alert("Server has been restarted :)");
        },
        (err) => {
            setTimeout(checkLife, 500);
        }
    );
}

async function pullChanges() {
    var response = await apiFunction("/admin/update");
    if (response.ERROR) {
        alert(response.ERROR);
    }
}