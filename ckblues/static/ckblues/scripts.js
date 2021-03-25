document.addEventListener("DOMContentLoaded", function() {
  // add click event to update email password buttons
  let updateButton = document.querySelector('#update-button');
    updateButton.addEventListener('click', function() {
      // run this function when button is clicked
      updateCredentials(updateButton);
    });
  });

// display update credentials form, hide other page elements in user dashboard
function updateCredentials(updateButton) {
  // disable submit button until user inputs new email or new password
  let submitUpdateButton = document.querySelector('#submit-update-button');
  submitUpdateButton.disabled = true;

  //display and hide page sections after user clicks update email/password button
  let updateSection = document.querySelector('#update-section');
  updateSection.style.display = 'block';
  let feedbackSection = document.querySelector('#feedback-section');
  feedbackSection.style.display = 'none';
  updateButton.style.display = 'none';

  // enable submit button if user types in new email address
  let email = document.querySelector('#email');
  // Listen for input to be typed into the input field
  email.onkeyup = () => {
    if (email.value.length > 0) {
      submitUpdateButton.disabled = false;
    }
    else {
      submitUpdateButton.disabled = true;
    }
  }

  // enable submit button if user types two new matching passwords
  let password = document.querySelector('#password');
  let confirmation = document.querySelector('#confirmation');
  // Listen for input to be typed into the input field
  confirmation.onkeyup = () => {
    if (password.value === confirmation.value && password.value.length !== 0) {
      submitUpdateButton.disabled = false;
    }
    else {
      submitUpdateButton.disabled = true;
    }
  }

  //get cancel update button and add event listener
  let cancel = document.querySelector('#cancel-update-button');
  cancel.addEventListener('click', function() {
    updateSection.style.display = 'none';
    feedbackSection.style.display = 'block';
    updateButton.style.display = 'block';
  })
}