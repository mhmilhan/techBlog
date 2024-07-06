let profileBtn = document.getElementById('profile-btn');
let profileForm = document.querySelector('.profile-form-container');
let closeBtn = document.getElementById('close-btn');
let overlay = document.querySelector('.overlay');


profileBtn.addEventListener('click', () => {
  profileForm.classList.remove("hidden");
  overlay.classList.remove("hidden");
});

closeBtn.addEventListener('click', () => {
  profileForm.classList.add("hidden");
  overlay.classList.add("hidden");
});




