from flask import Flask, render_template, request, send_file
from invoice_generator import generate_pdf, number_to_words
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('invoice.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    data = request.json
    invoice_number = data['invoice_number']
    delivery_date = data['delivery_date']
    vehicle_number = data['vehicle_number']
    quantity = float(data['quantity'])
    unit_price = float(data['unit_price'])
    total_price = quantity * unit_price
    
    # Generate PDF
    filename = f"Invoice_{invoice_number}.pdf"
    generate_pdf(
        invoice_number=invoice_number,
        delivery_date=delivery_date,
        vehicle_number=vehicle_number,
        quantity=quantity,
        unit_price=unit_price,
        total_price=total_price
    )
    
    return {'filename': filename}

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)