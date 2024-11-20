function softUniStudents(input) {
    let courses = {};

    input.forEach(line => {
        if (line.includes(':')) {
            let [courseName, capacity] = line.split(': ');
            capacity = Number(capacity);
            if (!courses[courseName]) {
                courses[courseName] = { capacity, students: [] };
            } else {
                courses[courseName].capacity += capacity;
            }
        } else {
            let [studentInfo, courseName] = line.split(' joins ');
            let [usernameCredits, email] = studentInfo.split(' with email ');
            let [username, credits] = usernameCredits.split('[');
            credits = Number(credits.slice(0, -1));
            
            if (courses[courseName] && courses[courseName].students.length < courses[courseName].capacity) {
                courses[courseName].students.push({ username, credits, email });
            }
        }
    });

    let sortedCourses = Object.entries(courses).sort((a, b) => b[1].students.length - a[1].students.length);

    for (let [courseName, course] of sortedCourses) {
        console.log(`${courseName}: ${course.capacity - course.students.length} places left`);
        course.students
            .sort((a, b) => b.credits - a.credits)
            .forEach(s => {
                console.log(`--- ${s.credits}: ${s.username}, ${s.email}`);
            });
    }
}
