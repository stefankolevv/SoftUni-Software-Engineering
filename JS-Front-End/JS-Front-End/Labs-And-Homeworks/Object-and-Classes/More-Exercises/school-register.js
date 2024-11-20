function schoolRegister(input) {
    let students = {};

    for (let line of input) {
        let [name, grade, score] = line
            .match(/Student name: (.*?), Grade: (\d+), Graduated with an average score: (\d+\.\d+)/)
            .slice(1);

        grade = Number(grade) + 1;
        score = Number(score);

        if (score >= 3) {
            if (!students[grade]) {
                students[grade] = [];
            }
            students[grade].push({ name, score });
        }
    }

    Object.keys(students)
        .sort((a, b) => a - b)
        .forEach(grade => {
            let studentList = students[grade];
            console.log(`${grade} Grade`);
            console.log(`List of students: ${studentList.map(s => s.name).join(', ')}`);
            let averageScore = studentList.reduce((acc, s) => acc + s.score, 0) / studentList.length;
            console.log(`Average annual score from last year: ${averageScore.toFixed(2)}`);
            console.log();
        });
}

// Test Case

schoolRegister([
    "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
        "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
        "Student name: George, Grade: 8, Graduated with an average score: 2.83",
        "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
        "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
        "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
        "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
        "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
        "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
        "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
        "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
        "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
]);
schoolRegister([
    'Student name: George, Grade: 5, Graduated with an average score: 2.75',
    'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
    'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
    'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
    'Student name: John, Grade: 9, Graduated with an average score: 2.90',
    'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
    'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
]);