const target = document.querySelector('header');
const redHeaderButton = document.querySelector('#red_header');

redHeaderButton.addEventListener('click', function() {
    target.classList.add('red');
});
