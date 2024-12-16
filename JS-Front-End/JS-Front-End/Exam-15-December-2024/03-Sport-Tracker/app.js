document.addEventListener('DOMContentLoaded', function () {
    // Select form fields & buttons:
    const fields = {
        workout: document.querySelector('#workout'),
        location: document.querySelector('#location'),
        date: document.querySelector('#date')
    };

    const addWorkoutButton = document.querySelector('#add-workout');
    const editWorkoutButton = document.querySelector('#edit-workout');
    const workoutList = document.querySelector('#list');

    let workouts = [];

    // Add workout to list -> 'Add Workout' is clicked:
    addWorkoutButton.addEventListener('click', function () {
        const workout = fields.workout.value.trim();
        const location = fields.location.value.trim();
        const date = fields.date.value.trim();

        if (!workout || !location || !date) {
            alert('Please fill in all fields!');
            return;
        }

        // Add the workout to the array
        workouts.push({ workout, location, date });

        // Clear fields only after adding workout
        fields.workout.value = '';
        fields.location.value = '';
        fields.date.value = '';

        renderWorkouts();
    });

    // Render all workouts
    function renderWorkouts() {
        workoutList.innerHTML = ''; // Clear the list... only once

        // Create and append workouts dynamically
        workouts.forEach(function (workoutData, index) {
            const workoutElement = document.createElement('div');
            workoutElement.classList.add('container');
            workoutElement.dataset.index = index;

            const workoutTitle = document.createElement('h2');
            workoutTitle.textContent = workoutData.workout;
            workoutElement.appendChild(workoutTitle);

            const workoutDate = document.createElement('h3');
            workoutDate.textContent = workoutData.date;
            workoutElement.appendChild(workoutDate);

            const workoutLocation = document.createElement('h3');
            workoutLocation.textContent = workoutData.location;
            workoutElement.appendChild(workoutLocation);

            const buttonsContainer = document.createElement('div');
            buttonsContainer.id = 'buttons-container';
            workoutElement.appendChild(buttonsContainer);

            // Edit button
            const changeButton = document.createElement('button');
            changeButton.textContent = 'Change';
            changeButton.classList.add('change-btn');
            changeButton.addEventListener('click', function () {
                editWorkout(workoutData, index);
            });
            buttonsContainer.appendChild(changeButton);

            // Delete button
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Done';
            deleteButton.classList.add('delete-btn');
            deleteButton.addEventListener('click', function () {
                deleteWorkout(index);
            });
            buttonsContainer.appendChild(deleteButton);

            workoutList.appendChild(workoutElement);
        });
    }

    // Edit workout:
    function editWorkout(workoutData, index) {
        fields.workout.value = workoutData.workout;
        fields.location.value = workoutData.location;
        fields.date.value = workoutData.date;

        // Disable add button, enable edit button
        addWorkoutButton.disabled = true;
        editWorkoutButton.disabled = false;

        // Update workout when 'Edit Workout' is clicked
        editWorkoutButton.addEventListener('click', function () {
            workoutData.workout = fields.workout.value;
            workoutData.location = fields.location.value;
            workoutData.date = fields.date.value;

            workouts[index] = workoutData;

            fields.workout.value = '';
            fields.location.value = '';
            fields.date.value = '';

            addWorkoutButton.disabled = false;
            editWorkoutButton.disabled = true;

            renderWorkouts();
        });
    }

    // Delete workout:
    function deleteWorkout(index) {
        workouts.splice(index, 1); // Remove workout by index
        renderWorkouts(); // Update the workout list
    }

    renderWorkouts();
});
