import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from num2words import num2words

# Constants
CUSTOMER = "Mr Adnan - A.L.U INTERNATIONAL"
PAYABLE_TO = "A.T COMMODITIES"

def get_user_inputs():
    """Collect user inputs for the invoice."""
    invoice_no = input("Enter Invoice No.: ")
    delivery_date = input("Enter Delivery Date (DD-MMM-YYYY): ")
    vehicle_no = input("Enter Vehicle No.: ")
    quantity = float(input("Enter Quantity (M/TON): "))
    unit_price = float(input("Enter Unit Price (Rs): "))
    return invoice_no, delivery_date, vehicle_no, quantity, unit_price

def generate_text_invoice(invoice_no, delivery_date, vehicle_no, quantity, unit_price, total):
    """Generate and print a formatted text invoice."""
    amount_in_words = num2words(total, lang='en_IN').title().replace("And", "") + " Rupees Only"
    
    invoice_text = f"""
{'='*60}
{'Invoice':^60}
{'Submitted on: ' + datetime.datetime.now().strftime('%d/%m/%Y'):^60}
{'='*60}

| {'Invoice for':<30} | {'Payable to':<20} | {'Invoice #':<8} |
| {CUSTOMER:<30} | {PAYABLE_TO:<20} | {invoice_no:<8} |
{'-'*60}

| {'Description':<20} | {'Delivery Date':<15} | {'Qty (M/TON)':>12} | {'Unit price':>12} | {'Total price':>12} |
| {'Coal (' + vehicle_no + ')':<20} | {delivery_date:<15} | {quantity:>12.3f} | {'Rs' + f'{unit_price:,.0f}':>12} | {'Rs' + f'{total:,.0f}':>12} |
{'-'*60}

Notes:
Rs{total:,.0f}

{amount_in_words}
{'='*60}
"""
    print(invoice_text)

def generate_pdf_invoice(invoice_no, delivery_date, vehicle_no, quantity, unit_price, total):
    """Generate a PDF invoice using reportlab with a 14-line vertical gap at the top."""
    amount_in_words = num2words(total, lang='en_IN').title().replace("And", "") + " Rupees Only"
    file_name = f"Invoice_{invoice_no}.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    # Add 14-line gap (14 * 12 = 168 points)
    elements.append(Spacer(1, 14 * 12))

    styles = getSampleStyleSheet()
    style_center = ParagraphStyle(name='Center', alignment=1, parent=styles['Normal'])

    # Invoice Title
    elements.append(Paragraph("Invoice", styles['Heading2']))
    elements.append(Paragraph(f"Submitted on: {datetime.datetime.now().strftime('%d/%m/%Y')}", style_center))
    elements.append(Spacer(1, 20))

    # Invoice Details Table
    details_data = [
        ['Invoice for', 'Payable to', 'Invoice #'],
        [CUSTOMER, PAYABLE_TO, invoice_no]
    ]
    details_table = Table(details_data, colWidths=[200, 150, 100])
    details_table.setStyle(TableStyle([
        ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 10),
        ('LINEBELOW', (0,0), (-1,0), 1, colors.black),
        ('LINEBELOW', (0,1), (-1,1), 1, colors.black),
    ]))
    elements.append(details_table)
    elements.append(Spacer(1, 20))

    # Items Table
    items_data = [
        ['Description', 'Delivery Date', 'Qty (M/TON)', 'Unit Price', 'Total Price'],
        [f'Coal ({vehicle_no})', delivery_date, f'{quantity:.3f}', f'Rs{unit_price:,.0f}', f'Rs{total:,.0f}']
    ]
    items_table = Table(items_data, colWidths=[120, 90, 80, 80, 90])
    items_table.setStyle(TableStyle([
        ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 10),
        ('LINEBELOW', (0,0), (-1,0), 1, colors.black),
        ('LINEBELOW', (0,1), (-1,1), 1, colors.black),
        ('ALIGN', (2,0), (-1,-1), 'RIGHT'),
    ]))
    elements.append(items_table)
    elements.append(Spacer(1, 20))

    # Total Amount
    elements.append(Paragraph("Notes:", styles['Normal']))
    elements.append(Paragraph(f"Rs{total:,.0f}", styles['Normal']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(amount_in_words, styles['Normal']))

    # Build PDF
    doc.build(elements)
    print(f"PDF invoice saved as '{file_name}'")

def main():
    invoice_no, delivery_date, vehicle_no, quantity, unit_price = get_user_inputs()
    total = quantity * unit_price
    generate_text_invoice(invoice_no, delivery_date, vehicle_no, quantity, unit_price, total)
    generate_pdf_invoice(invoice_no, delivery_date, vehicle_no, quantity, unit_price, total)

if __name__ == "__main__":
    main()
