function authenticate() {
    var url = "http://" + location.host + "/authentication/login";
    var request = JSON.stringify(
        { 
            "USER_NAME": getCookie("username"),
            "PASSWORD": getCookie("password")
        }
    );

    return new Promise(resolve => {
        sendPost(url, request, debug, function(response) {
            resolve(response);
        });
    });
}