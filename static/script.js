function hideResult() {
  const resultDiv = document.querySelector('.result');
  if (resultDiv) {
    resultDiv.style.display = 'none';
  }
}

document.addEventListener('click', function (event) {
  const resultDiv = document.querySelector('.result');
  const form = document.querySelector('form');
  if (resultDiv && !form.contains(event.target)) {
    hideResult();
  }
});

document.getElementById('generate-password').addEventListener('click', function () {
  const formDiv = document.getElementById('generate-password-form');
  formDiv.style.display = 'flex';
  const formDiv2 = document.getElementById('generate-password-button');
  formDiv2.style.display = 'block';
});

document.getElementById('submit-password-generation').addEventListener('click', function (event) {
  event.preventDefault();

  const length = parseInt(document.getElementById('length').value);
  const userCharset = document.getElementById('user_chars').value;

  fetch('/generate_password', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ length: length, user_charset: userCharset }),
  })
  .then(response => response.json())
  .then(data => {
    if (data.error) {
      alert(data.error);
    } else {
      const passwordField = document.getElementById('password');
      passwordField.value = data.password;
      hideResult();
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
});