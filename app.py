from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/custom_window')
def custom_window():
    return render_template('custom_window.html')

@app.route('/bulk_order')
def bulk_order():
    return render_template('bulk_order.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        width = float(request.form['width'])
        height = float(request.form['height'])
        quantity = int(request.form['quantity'])
        rate_per_sqm = float(request.form['rate'])
        unit = request.form['unit']

        # Convert inches to centimeters if necessary
        if unit == "in":
            width *= 2.54
            height *= 2.54

        # Calculate area in square meters and cost
        area_sqm = (width * height) / 10000 * quantity
        cost = area_sqm * rate_per_sqm

        # Capture current date and time
        current_date = datetime.now().strftime("%b-%d-%Y")
        current_time = datetime.now().strftime("%I:%M %p")

        # Return the data as JSON
        return jsonify({
            "date": current_date,
            "time": current_time,
            "width": f"{width:.2f} {unit}",
            "height": f"{height:.2f} {unit}",
            "quantity": quantity,
            "area_sqm": f"{area_sqm:.2f}",
            "cost": f"${cost:.2f}"
        })
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
