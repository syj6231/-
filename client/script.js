document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // 폼의 기본 동작(페이지 새로고침)을 막습니다.

    const formData = new FormData();
    formData.append('musicFile', document.getElementById('musicFile').files[0]);

    try {
        const response = await fetch('http://localhost:5000/analyze', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();
        document.getElementById('result').innerText = JSON.stringify(result);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = "Error uploading file.";
    }
});