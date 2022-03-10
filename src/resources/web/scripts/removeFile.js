function removeFile(fileName) {
    if (confirm("Opravdu mám smazat " + fileName + " ze serveru?\nOperace je nevratná.")) {
        window.location.href = "files/delete/" + fileName;
    }
}