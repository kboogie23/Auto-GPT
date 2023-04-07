// Handle the button click event to check for spam
function checkForSpam() {

  // TODO: Implement code to check for spam and move to deleted if spam is detected.
  alert('Spam check not yet implemented!');
}

// Add an event listener to the button to check for spam on click
window.addEventListener('load', function() {
  document.getElementById('checkSpamButton').addEventListener('click', checkForSpam);
});