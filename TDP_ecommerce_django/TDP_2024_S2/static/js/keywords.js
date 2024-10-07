document.addEventListener('DOMContentLoaded', function() {
    const tagInput = document.getElementById('tagInput');
    const tagContainer = document.getElementById('tagContainer');
    const generateBtn = document.getElementById('generateButton');

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

    generateBtn.addEventListener('click', function() {
        const generatedWords = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'];
        generatedWords.forEach(word => {
            tagInput.value = word;
            const enterEvent = new KeyboardEvent('keypress', { key: 'Enter' });
            tagInput.dispatchEvent(enterEvent); // Trigger the 'Enter' event automatically
        });
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