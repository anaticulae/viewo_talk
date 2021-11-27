const API = '/api/v0'

const rpc = function (url, callback, error = undefined) {
    let call = `${API}${url}`
    $.ajax(call, {
        dataType: 'json',
        success: function (response) {
            callback(response)
        },
        error: function (response) {
            if (error != undefined) {
                error()
            } else {
                console.log(`error: ${call}`);
            }
        }
    });
}
