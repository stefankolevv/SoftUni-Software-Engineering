function solve() {
    
    const searchStr = document.querySelector('#searchField').value.toLowerCase().trim();
    const students = document.querySelectorAll('table tbody tr');

    if (searchStr == '') return;

    students.forEach(student => {

        console.log( student.textContent );

        student.classList.remove('select');

        if ( student.textContent.toLowerCase().includes(searchStr) ) {
            student.classList.add('select');
        }
    });

}