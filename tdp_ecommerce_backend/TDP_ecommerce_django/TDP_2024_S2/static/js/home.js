document.addEventListener('DOMContentLoaded', function() {
    
    tagInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            const tagText = tagInput.value.trim();
            if (tagText !== "") {
                createTag(tagText);
                tagInput.value = ''; // Empties the input after creating the tag
            }
            event.preventDefault(); // Prevent form submission if inside a form
        }
    });

    function createTag(text) {
        const tag = document.createElement('div');
        tag.className = 'tag';
        tag.innerHTML = text;

        const input = document.createElement('input');
        input.type = 'hidden';
        input.id = 'keywords';
        input.name = 'keywords';
        input.value = text;

        const closeBtn = document.createElement('span');
        closeBtn.className = 'close-btn';
        closeBtn.innerText = '✖';
        closeBtn.addEventListener('click', function() {
            tag.remove();
        });

        tag.appendChild(closeBtn);
        tag.appendChild(input);
        tagContainer.appendChild(tag);
    }
});