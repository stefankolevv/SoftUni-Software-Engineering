async function lockedProfile() {
    const main = document.getElementById('main');

    const response = await fetch('http://localhost:3030/jsonstore/advanced/profiles');
    const profiles = await response.json();

    main.innerHTML = '';

    Object.values(profiles).forEach((profile, index) => {
        const profileDiv = document.createElement('div');
        profileDiv.className = 'profile';

        profileDiv.innerHTML = `
            <img src="./iconProfile2.png" class="userIcon" />
            <label>Lock</label>
            <input type="radio" name="user${index}Locked" value="lock" checked>
            <label>Unlock</label>
            <input type="radio" name="user${index}Locked" value="unlock"><br>
            <hr>
            <label>Username</label>
            <input type="text" name="user${index}Username" value="${profile.username}" disabled readonly />
            <div class="user${index}Details" style="display: none;">
                <hr>
                <label>Email:</label>
                <input type="email" name="user${index}Email" value="${profile.email}" disabled readonly />
                <label>Age:</label>
                <input type="number" name="user${index}Age" value="${profile.age}" disabled readonly />
            </div>
            <button>Show more</button>
        `;

        const button = profileDiv.querySelector('button');
        const detailsDiv = profileDiv.querySelector(`.user${index}Details`);
        const lockRadio = profileDiv.querySelector(`input[name="user${index}Locked"][value="lock"]`);

        button.addEventListener('click', () => {
            if (!lockRadio.checked) {
                if (detailsDiv.style.display === 'none') {
                    detailsDiv.style.display = 'block';
                    button.textContent = 'Hide it';
                } else {
                    detailsDiv.style.display = 'none';
                    button.textContent = 'Show more';
                }
            }
        });

        main.appendChild(profileDiv);
    });
}
