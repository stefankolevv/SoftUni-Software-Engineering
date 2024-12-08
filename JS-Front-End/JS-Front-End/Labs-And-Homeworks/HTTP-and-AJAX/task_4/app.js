function loadStudents(baseUrl, onSuccess) {
  fetch(baseUrl)
      .then(response => response.json())
      .then(onSuccess)
      .catch(error => console.error('Error: ', error));
}

function createStudent(baseUrl, student, onSuccess) {
  fetch(baseUrl, {
      method: 'POST',
      body: JSON.stringify(student)
  })
      .then(response => response.json())
      .then(onSuccess)
      .catch(error => console.error('Error: ', error));    
}

function createElement(tag, properties, container = null){
  
  const element = document.createElement(tag);

  Object.keys(properties).forEach(key => {
      if ( typeof properties[key] === 'object' ) {
          Object.assign( element.dataset, properties[key] )
      } else {
          element[key] = properties[key];
      }
  });

  if ( container ) container.append( element );

  return element;
}


function init() {
  
  const baseUrl = 'http://localhost:3030/jsonstore/collections/students';

  const buttonCreateEl = document.querySelector('#submit');
  const listEl = document.querySelector('table tbody');
          
  function createEntry({ firstName, lastName, facultyNumber, grade }) {
      const entryEl = createElement('tr', {}, listEl);
      createElement('td', { textContent: firstName }, entryEl);
      createElement('td', { textContent: lastName }, entryEl);
      createElement('td', { textContent: facultyNumber }, entryEl);
      createElement('td', { textContent: grade }, entryEl);
  }

  function createEntryHandler(e) {

      const inputs = document.querySelectorAll('.inputs input');

      const [ firstName, lastName, facultyNumber, grade ] = [...inputs].map(field => field.value);

      if ( ! firstName || ! lastName || ! facultyNumber || ! grade ) return;
      
      const student = { firstName, lastName, facultyNumber, grade  };

      createStudent(baseUrl, student, (result) => {
          createEntry(result);
      });
  }

  loadStudents(baseUrl, (result) => {
      Object.values(result).forEach(createEntry);
  });

  buttonCreateEl.addEventListener('click', createEntryHandler);
  
}

document.addEventListener('DOMContentLoaded', init);