

// Clicks current course
function findCurrentCourse() {
    current_course = Array.from(document.querySelectorAll('.bluebdr'))[0];
    console.log(current_course);
    current_course.getElementsByTagName('button')[0].click();
}
findCurrentCourse();




//To click on mark as complete

async function markAsComplete() {
    const parent = document.querySelector('.contentlist_sec');
    if (!parent) {
        console.error('Parent element not found');
        return;
    }
    // changed: only immediate div children
    const ids = Array.from(parent.children)
        .filter(el => el.tagName === 'DIV' && el.id)
        .map(div => div.id);
    //console.log(ids);
    for (const id of ids) {

        new_id = parseInt(id.replace('pro_', ''));
        console.log(new_id);
        mark_as_complete_hub_product(new_id);
        await new Promise(resolve => setTimeout(resolve, 2000));
    }
}
markAsComplete();



//To launch quiz
function launch_quiz() {
    const buttons = document.querySelectorAll('a[data-45="Launch"]');
    buttons.forEach(button => button.click());
}
launch_quiz();


//To find answers during quiz
async function find_answers() {

    //To click the answers
    function clickById(qid, id) {
        const partial_id = `_${qid}_${id}`;
        // select all elements whose id ends with partial_id
        const elems = Array.from(document.querySelectorAll(`[id$="${partial_id}"]`));
        if (!elems.length) {
            console.error(`No elements ending with "${partial_id}" found`);
            return;
        }
        elems.forEach(el => el.click());
    }
    questions_data.forEach((question, index) => {
        question_data = "Question " + (index + 1) + " answers are option's : "
        question.all_options.forEach((option, index) => {
            if (option.is_true == 1) {
                question_data += index + 1 + " , "
                if (question.questions_type == "Multiple")
                {
                    clickById(question.ques_id, `_${index}`);
                }
                clickById(question.ques_id, option.answer_id);
            }
        })
        console.log(question);
        //page_change(index +1);
    });

    //To click on submit quiz button   
    const buttons = document.querySelectorAll('.submit_quiz_btn');
    buttons.forEach(button => button.click());

    //To move onto results page
    toc_click();

    //To wait for 30-50 seconds to load the results page and to make it human like timing
    const randomTime = Math.floor(Math.random() * (50000 - 30000 + 1)) + 30000;
    await new Promise(resolve => setTimeout(resolve, randomTime));
    //To click process results button
    const result_buttons = document.querySelectorAll('.retake_quiz_btn');
    result_buttons.forEach(button => button.click());

}
find_answers();


