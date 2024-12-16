window.addEventListener("load", solve);

function solve() {
  function createElement(tag, properties, container) {
      const element = document.createElement(tag);
      Object.keys(properties).forEach(key => {
          if (typeof properties[key] === 'object') {
              Object.assign(element[key], properties[key]);
          } else {
              element[key] = properties[key];
          }
      });
      if (container) container.appendChild(element);
      return element;
  }

  const emailField = document.querySelector('#email');
  const eventField = document.querySelector('#event');
  const locationField = document.querySelector('#location');
  const nextButton = document.querySelector('#next-btn');

  const previewList = document.querySelector('#preview-list');
  const eventList = document.querySelector('#event-list');

  nextButton.addEventListener('click', () => { // Adding an event listener that handles a click on the 'Next' button...
      const email = emailField.value.trim();
      const eventName = eventField.value.trim();
      const location = locationField.value.trim();

      if (!email || !eventName || !location) {
          return;
      }

      const listItem = createElement('li', {}, previewList);

      const article = createElement('article', {}, listItem);
      createElement('h4', { textContent: `Organizer: ${email}` }, article);
      createElement('p', { textContent: `Event: ${eventName}` }, article);
      createElement('p', { textContent: `Location: ${location}` }, article);

      const editButton = createElement('button', { textContent: 'Edit', className: 'action-btn edit', onclick: editHandler }, listItem);
      const applyButton = createElement('button', { textContent: 'Apply', className: 'action-btn apply', onclick: applyHandler }, listItem);

      emailField.value = '';
      eventField.value = '';
      locationField.value = '';
      nextButton.disabled = true;
  });

  // Adding 2 functions: editHandler - returns the values ​​back to the form; applyHandler - moves the event to the approved list:
  function editHandler(event) {
      const listItem = event.target.parentElement;

      const email = listItem.querySelector('h4').textContent.replace('Organizer: ', '');
      const eventName = listItem.querySelectorAll('p')[0].textContent.replace('Event: ', '');
      const location = listItem.querySelectorAll('p')[1].textContent.replace('Location: ', '');

      emailField.value = email;
      eventField.value = eventName;
      locationField.value = location;

      listItem.remove();
      nextButton.disabled = false;
  }

  function applyHandler(event) {
      const listItem = event.target.parentElement;

      listItem.querySelector('.edit').remove();
      listItem.querySelector('.apply').remove();

      eventList.appendChild(listItem);
      nextButton.disabled = false;
  }
}