// ============================
// C O O K I E  S T U F F
// ============================

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// ============================
// M O D A L S
// ============================
document.addEventListener('DOMContentLoaded', () => {
    // Functions to open and close a modal
    function openModal($el) {
      $el.classList.add('is-active');
    }
  
    function closeModal($el) {
      $el.classList.remove('is-active');
    }
  
    function closeAllModals() {
      (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
      });
    }
  
    // Add a click event on buttons to open a specific modal
    (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);
      console.log($target);
  
      $trigger.addEventListener('click', () => {
        openModal($target);
      });
    });
  
    // Add a click event on various child elements to close the parent modal
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
      const $target = $close.closest('.modal');
  
      $close.addEventListener('click', () => {
        closeModal($target);
      });
    });
  
    // Add a keyboard event to close all modals
    document.addEventListener('keydown', (event) => {
      const e = event || window.event;
  
      if (e.keyCode === 27) { // Escape key
        closeAllModals();
      }
    });
  });


// ====================================
// N E W  C U R R I C U L U M  F O R M
// ====================================

let curriculumForm = document.querySelector('#curriculum-form')
const curriculumURL = '/api/curriculum/new'

curriculumForm.addEventListener('submit', function(event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(curriculumForm)
    fetch(curriculumURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })

    window.location.reload()
})


// ====================================
// N E W  S T U D E N T  F O R M
// ====================================

let studentForm = document.querySelector('#student-form')
const studentURL = '/api/student/new'

studentForm.addEventListener('submit', function(event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(studentForm)
    fetch(studentURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })

    window.location.reload()
})


// ====================================
// N E W  W O R D  F O R M
// ====================================

let wordForm = document.querySelector('#word-form')
const wordURL = '/api/word/new'

wordForm.addEventListener('submit', function(event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(wordForm)
    fetch(wordURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })

    window.location.reload()
})


// ====================================
// N E W  C O N C E P T  F O R M
// ====================================

let conceptForm = document.querySelector('#concept-form')
const conceptURL = '/api/concept/new'

conceptForm.addEventListener('submit', function(event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(conceptForm)
    fetch(conceptURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })

    window.location.reload()
})


// ====================================
// N E W  G A M E  F O R M
// ====================================

let gameForm = document.querySelector('#game-form')
const gameURL = '/api/game/new'

gameForm.addEventListener('submit', function(event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(gameForm)
    fetch(gameURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })

    window.location.reload()
})


// ====================================
// N E W  O B J E C T I V E  F O R M
// ====================================

let objectiveForm = document.querySelector('#objective-form')
const objectiveURL = '/api/objective/new'

objectiveForm.addEventListener('submit', function(event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(objectiveForm)
    fetch(objectiveURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })

    window.location.reload()
})


// ====================================
// P E R S O N A L  N O T E S
// ====================================

// TO DO: Get all new objects to populate without page reload; figure out a way to make this all DRY; Get edit and delete functionality also working via AJAX rather than on separate pages
