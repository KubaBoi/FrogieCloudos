
async function buildSettingTable() {
    response = await callEndpoint("GET", "/admin/getSettings");
    if (!response.ERROR) {
        for (const key in response) {
            if (response.hasOwnProperty(key)) {
                addSetting(key, response[key]);
            }
        }
        document.title = "CHAdmin - " + response.name;
    }
}

function addSetting(setting, value) {
    var table = document.querySelector("#settingsTable");

    var row = document.createElement("tr");
    var nameColumn = document.createElement("td");
    var valueColumn = document.createElement("td");

    nameColumn.innerHTML = setting;
    if (setting == "dbPassword")
        valueColumn.innerHTML = "<input type='password' value='" + value + "'>";
    else
        valueColumn.innerHTML = "<input type='text' value='" + value + "'>";
    
    row.appendChild(nameColumn);
    row.appendChild(valueColumn);
    table.appendChild(row);
}