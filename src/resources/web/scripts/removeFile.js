function removeFile(fileName) {
    if (confirm("Opravdu mám smazat " + fileName + " ze serveru?\nOperace je nevratná.")) {
        window.location.href = "/delete/files/" + fileName;
    }
}