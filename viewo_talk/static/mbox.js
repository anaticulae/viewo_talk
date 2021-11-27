const WAITFOR = 5.0

const listen = function () {
    rpc(`/talktome`, function (response) {
        let messages = response.messages
        for (let message of messages) {
            mbox_show(message.title, message.content)
        }
        setTimeout(() => listen(), WAITFOR * 1000);
    })
}

const mbox_hide = function () {
    $('#mbox').addClass('hidden')
}

const mbox_show = function (headline, content) {
    $('#mbox_headline').text(headline)
    $('#mbox_content').text(content)
    $('#mbox').removeClass('hidden')
}

$(document).ready(function () {
    $(`#mbox_close`).click(function () {
        mbox_hide()
    });
    listen()
})
