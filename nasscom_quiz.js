async function find_answers() {
    function clickById(qid, id) {
        const partial_id = `_${qid}_${id}`
        const elems = Array.from(document.querySelectorAll(`[id$="${partial_id}"]`))
        if (!elems.length) {
            console.error(`No elements ending with "${partial_id}" found`)
            return
        }
        elems.forEach(el => el.click())
    }
    questions_data.forEach((question, index) => {
        question_data = "Question " + (index + 1) + " answers are option's : "
        question.all_options.forEach((option, index) => {
            if (option.is_true == 1) {
                question_data += index + 1 + " , "
                if (question.questions_type == "Multiple")
                {
                    clickById(question.ques_id, `_${index}`)
                }
                else
                {
                clickById(question.ques_id, option.answer_id)
                }
            }
        })
        console.log(question)
    })
    const buttons = document.querySelectorAll('.submit_quiz_btn')
    buttons.forEach(button => button.click())
    toc_click()
   
}find_answers()
