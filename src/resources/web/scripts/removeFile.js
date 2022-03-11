async function removeFile(fileName) {
    if (confirm("Opravdu mám smazat " + fileName + " ze serveru?\nOperace je nevratná.")) {
        response = await remove(fileName);
        if (response.ERROR == null) {
            buildTable();
        }
    }
}

function remove(fileName) {
    var url = "/fileController/delete";
    var request = JSON.stringify(
        { 
            "TOKEN": getCookie("token"),
            "FILE_NAME": fileName
        }
    );

    return new Promise(resolve => {
        sendPost(url, request, debug, function(response) {
            resolve(response);
        });
    });
}