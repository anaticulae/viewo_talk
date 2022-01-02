const WAITFOR = 5.0

const listen = function () {
    rpc(`/talktome`, function (response) {
        let messages = response.messages
        if (messages != undefined) {
            evaluate_messages(messages)
        }
        setTimeout(() => listen(), WAITFOR * 1000);
    })
}

const evaluate_messages = function (messages) {
    for (let message of messages) {
        if (message.name == 'MESSAGE') {
            mbox_show_info(message.title, message.content)
        } else if (message.name == 'QUESTION') {
            mbox_show_question(message.title, message.content, message.index)
        }
    }
}

const mbox_hide = function () {
    $('#mbox').addClass('hidden')
}

const mbox_show_info = function (headline, content) {
    $('#mbox_question').addClass('hidden')
    $('#mbox_headline').text(headline)
    $('#mbox_content').text(content)
    $('#mbox').removeClass('hidden')
}

const mbox_show_question = function (headline, question, index) {
    QUESTION = index
    $('#mbox_question').removeClass('hidden')
    $('#mbox_headline').text(headline)
    $('#mbox_content').text(question)
    $('#mbox').removeClass('hidden')
}

let QUESTION = null

const register = function () {
    $(`#mbox_close`).click(function () {
        mbox_hide()
    });
    $(`#mbox_question_yes`).click(function () {
        rpc_post('/talktome', {
            question: QUESTION,
            answer: 1,
        })
        mbox_hide()
    });
    $(`#mbox_question_no`).click(function () {
        rpc_post('/talktome', {
            question: QUESTION,
            answer: 0,
        })
        mbox_hide()
    });
}

$(document).ready(function () {
    register()
    // start after 3 seconds
    setTimeout(() => listen(), 3000);
})
