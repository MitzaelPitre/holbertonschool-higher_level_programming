const target = document.querySelector('header');
const updateHeaderButton = document.querySelector('#update_header');

updateHeaderButton.addEventListener('click', function() {
    target.textContent = 'New Header!!!';
});
