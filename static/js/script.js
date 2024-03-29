// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    // Form submission for insurance cost prediction
    document.getElementById('predictionForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        
        // Get form data
        const formData = new FormData(this);
        
        // Send POST request to /predict endpoint
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Show popup with predicted price
            const popup = document.getElementById('popup');
            const predictionResult = document.getElementById('predictionResult');
            predictionResult.textContent = `Estimated medical insurance cost: ${data.prediction.toFixed(2)} INR`;
            popup.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });

    // Close the popup when close button is clicked
    document.getElementById('close').addEventListener('click', function() {
        document.getElementById('popup').style.display = 'none';
    });

    // Form submission for login
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Perform login actions here
    });
});
