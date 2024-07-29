const socket = io.connect('http://127.0.0.1:8000');

socket.on('message', function(data) {
    console.log(data);
});

socket.on('response', function(data) {
    console.log(data);
});

function getNextQuestion() {
    fetch('/api/questions/1')
        .then(response => response.json())
        .then(data => {
            document.getElementById('question').innerText = data.question;
        })
        .catch(error => console.error('Error:', error));
}
