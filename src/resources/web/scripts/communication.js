function sendPost(url, jsonRequest, output, callback) {
    var xhttp = new XMLHttpRequest(); 
    
    var date = new Date();
    if (output) console.log("SENDING", date.getTime(), url, jsonRequest);

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            json = JSON.parse(this.responseText);
            if(output) console.log("RESPONSE", date.getTime(), url, json);
            if(callback) callback(json);
        }
    };
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(jsonRequest);
}

function sendGet(url, output, callback) {
    var xmlHttp = new XMLHttpRequest();

    var date = new Date();
    if (output) console.log("SENDING", date.getTime(), url);

    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4) {
            json = JSON.parse(this.responseText);
            if(output) console.log("RESPONSE", date.getTime(), url, json);
            if(callback) callback(json);
        }
    }
    xmlHttp.open("GET", url, true); // true for asynchronous 
    xmlHttp.send(null);
}