document.addEventListener("DOMContentLoaded", function() {
  // add click event to dimiss welcome link
  let dismiss = document.querySelector('#dismiss');
    dismiss.addEventListener('click', function() {
      //run function when dismiss clicked
      dismissWelcome(dismiss);
    });
  });

function dismissWelcome(dismiss) {
  document.querySelector("#welcome").style.display = 'none';
  
}