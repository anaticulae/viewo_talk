const WAITFOR = 5.0

const listen = function () {
    rpc(`/talktome`, function (response) {
        let messages = response.messages
        for (let message of messages) {
            if (message.name == 'MESSAGE') {
                mbox_show_info(message.title, message.content)
            } else if (message.name == 'QUESTION') {
                mbox_show_question(message.title, message.content)
            }
        }
        setTimeout(() => listen(), WAITFOR * 1000);
    })
}

const mbox_hide = function () {
    $('#mbox').addClass('hidden')
}

const mbox_show_info = function (headline, content) {
    $('#mbox_content').removeClass('hidden')
    $('#mbox_question').addClass('hidden')
    $('#mbox_headline').text(headline)
    $('#mbox_content').text(content)
    $('#mbox').removeClass('hidden')
}

const mbox_show_question = function (headline, question) {
    $('#mbox_content').addClass('hidden')
    $('#mbox_question').removeClass('hidden')
    $('#mbox_headline').text(headline)
    $('#mbox_question').text(question)
    $('#mbox').removeClass('hidden')
}

$(document).ready(function () {
    $(`#mbox_close`).click(function () {
        mbox_hide()
    });
    listen()
})
