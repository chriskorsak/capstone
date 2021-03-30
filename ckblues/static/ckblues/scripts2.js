// create 'firstVisit' and set to 0 if not present
if (!localStorage.getItem('firstVisit')) {
  localStorage.setItem('firstVisit', 0);
}

// allow user who isn't logged in to dismiss welcome message at top of index page and not reappear
document.addEventListener("DOMContentLoaded", function() {
  let dismiss = document.querySelector('#dismiss');
    //dismiss element will be present on page to add click event
    if (dismiss !== null) {
      let firstVisit = localStorage.getItem('firstVisit');
      if (firstVisit > 0) {
        document.querySelector("#welcome").style.display = 'none';
      }
      // add click event to dismiss
      dismiss.addEventListener('click', function() {
        // increment firstVisit so user won't see welcome again in future
        localStorage.setItem('firstVisit', 1);
        // hide welcome after dissmissing
        document.querySelector("#welcome").style.display = 'none';
      });
    }
  });