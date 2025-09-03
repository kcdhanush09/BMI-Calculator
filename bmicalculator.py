from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Route to serve your HTML frontend
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>BMI Calculator</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                max-width: 500px; 
                margin: 50px auto; 
                padding: 20px;
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                width: 100%;
            }
            h2 {
                text-align: center;
                color: #333;
                margin-bottom: 20px;
            }
            .input-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: 600;
                color: #333;
            }
            input {
                width: 100%;
                padding: 12px;
                border: 2px solid #ddd;
                border-radius: 8px;
                font-size: 16px;
            }
            input:focus {
                border-color: #2575fc;
                outline: none;
            }
            button {
                width: 100%;
                padding: 15px;
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 18px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s;
            }
            button:hover {
                transform: translateY(-2px);
            }
            .result {
                margin-top: 25px;
                padding: 20px;
                background: #f8f9fa;
                border-radius: 10px;
                text-align: center;
                display: none;
            }
            .bmi-value {
                font-size: 32px;
                font-weight: bold;
                color: #6a11cb;
                margin: 10px 0;
            }
            .category {
                font-size: 18px;
                font-weight: 600;
                padding: 8px;
                border-radius: 5px;
            }
            .underweight { color: #ff9800; background: #fff3e0; }
            .normal { color: #4caf50; background: #e8f5e9; }
            .overweight { color: #ff5722; background: #ffebee; }
            .obese { color: #d32f2f; background: #ffebee; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>BMI Calculator</h2>
            <form onsubmit="calculateBMI(event)">
                <div class="input-group">
                    <label for="weight">Weight (kg):</label>
                    <input type="number" id="weight" step="0.1" placeholder="e.g., 68.5" required>
                </div>
                <div class="input-group">
                    <label for="height">Height (m):</label>
                    <input type="number" id="height" step="0.01" placeholder="e.g., 1.75" required>
                </div>
                <button type="submit">Calculate BMI</button>
            </form>
            
            <div class="result" id="result">
                <h3>Your BMI Result</h3>
                <div class="bmi-value" id="bmi-value">23.4</div>
                <div class="category" id="category">Normal weight</div>
            </div>
        </div>
        
        <script>
            function calculateBMI(event) {
                event.preventDefault();
                const weight = document.getElementById('weight').value;
                const height = document.getElementById('height').value;
                
                fetch('/calculate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ weight: weight, height: height })
                })
                .then(response => response.json())
                .then(data => {
                    const resultDiv = document.getElementById('result');
                    const bmiValue = document.getElementById('bmi-value');
                    const category = document.getElementById('category');
                    
                    bmiValue.textContent = data.bmi;
                    category.textContent = data.category;
                    category.className = 'category ' + data.category.toLowerCase().replace(' ', '-');
                    
                    resultDiv.style.display = 'block';
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error calculating BMI. Please try again.');
                });
            }
        </script>
    </body>
    </html>
    """

# API endpoint to calculate BMI
@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    try:
        data = request.json
        weight = float(data['weight'])
        height = float(data['height'])
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        bmi = round(bmi, 1)
        
        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        return jsonify({'bmi': bmi, 'category': category})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
