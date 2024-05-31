const target = document.querySelector('header');
const toggleHeaderButton = document.querySelector('#toggle_header');

toggleHeaderButton.addEventListener('click', function() {
    if (target.classList.contains('red')) {
        target.classList.remove('red');
        target.classList.add('green');
    } else {
        target.classList.remove('green');
        target.classList.add('red');
    }
});
