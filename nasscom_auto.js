// Clicks current course
function findCurrentCourse() {
    current_course = Array.from(document.querySelectorAll('.bluebdr'))[0];
    console.log(current_course);
    current_course.getElementsByTagName('button')[0].click();
}





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




//To launch quiz
function launch_quiz() {
    const buttons = document.querySelectorAll('a[data-45="Launch"]');
    buttons.forEach(button => button.click());
}




