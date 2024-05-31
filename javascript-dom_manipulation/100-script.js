document.addEventListener('DOMContentLoaded', function() {
    const addItemButton = document.getElementById('add_item');
    const removeItemButton = document.getElementById('remove_item');
    const clearListButton = document.getElementById('clear_list');
    const myList = document.querySelector('.my_list');

    addItemButton.addEventListener('click', function() {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';
        myList.appendChild(newItem);
    });

    removeItemButton.addEventListener('click', function() {
        const items = myList.querySelectorAll('li');
        if (items.length > 0) {
            const lastItem = items[items.length - 1];
            myList.removeChild(lastItem);
        }
    });

    clearListButton.addEventListener('click', function() {
        myList.innerHTML = '';
    });
});
