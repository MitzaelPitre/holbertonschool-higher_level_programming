document.addEventListener('DOMContentLoaded', function() {
  const translateButton = document.getElementById('btn_translate');
  const languageSelect = document.getElementById('language_code');
  const helloElement = document.getElementById('hello');

  translateButton.addEventListener('click', function() {
    const languageCode = languageSelect.value;
    if (languageCode !== '') {
      fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
        .then(response => response.json())
        .then(data => {
          helloElement.textContent = data.hello;
        })
        .catch(error => console.error('Error fetching translation:', error));
    } else {
      helloElement.textContent = 'Please select a language';
    }
  });
});
