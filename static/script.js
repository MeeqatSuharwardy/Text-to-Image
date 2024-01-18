document.getElementById('promptForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const prompt = document.getElementById('promptInput').value;
    fetch('/generate-image', {
        method: 'POST',
        body: new URLSearchParams({ 'prompt': prompt })
    })
    .then(response => response.json())
    .then(data => {
        const img = document.getElementById('generatedImage');
        img.src = 'data:image/jpeg;base64,' + data.image;
        img.style.display = 'block';
    });
});
