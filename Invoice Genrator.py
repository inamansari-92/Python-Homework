# # Invoice Generator for A.T Commodities (Copilot Version)
#----------------------------------------------------------------

# def generate_invoice():
#     # Static Info
#     company_name = "A.T Commodities"
#     address = "C-2 WESTLAND TRADE CENTER SHAHEED E MILLAT ROAD, KARACHI."
#     phone = "021-34381222"
#     website = "www.atcommodities.pk"
#     invoice_for = "Mr. Talha Niazi Sb - Niazi Bricks"
#     payable_to = "A.T COMMODITIES"
#     description = "Coal"
#     # Dynamic Input
#     invoice_no = input("Enter Invoice No.: ")
#     delivery_date = input("Enter Delivery Date (e.g. 29-May-2025): ")
#     vehicle_no = input("Enter Vehicle Number: ")
#     quantity = float(input("Enter Quantity (M/TON): "))
#     unit_price = float(input("Enter Unit Price (Rs): "))
#     total_price = quantity * unit_price
#     # Output Invoice
#     print("\n" + "="*60)
#     print(f"{company_name}")
#     print(address)
#     print(f"Phone: {phone} | Website: {website}")
#     print("="*60)
#     print(f"Invoice for: {invoice_for}")
#     print(f"Payable to: {payable_to}")
#     print(f"Invoice No.: {invoice_no}")
#     print("-"*60)
#     print(f"Description: {description} (Vehicle no: {vehicle_no})")
#     print(f"Delivery Date: {delivery_date}")
#     print(f"Qty (M/TON): {quantity:.3f}")
#     print(f"Unit Price: Rs{unit_price:,.2f}")
#     print(f"Total Price: Rs{total_price:,.0f}")
#     print("="*60)
# # Run it
# generate_invoice()

# Invoice Generator for A.T Commodities (Chatgpt Version)
#----------------------------------------------------------------

# from datetime import datetime

# # Static company and customer info
# company_name = "A.T COMMODITIES"
# company_address = "C-2 WESTLAND TRADE CENTER\nSHAHEED E MILLAT ROAD, KARACHI"
# phone_number = "021-34381222"
# website = "www.atcommodities.pk"
# payable_to = "A.T COMMODITIES"
# invoice_for = "Mr. Talha Niazi Sb\nNiazi Bricks"

# # Input from user
# invoice_no = input("Enter Invoice No.: ")
# delivery_date = input("Enter Delivery Date (e.g., 29-May-2025): ")
# vehicle_number = input("Enter Vehicle Number: ")
# quantity = float(input("Enter Quantity (M/TON): "))
# unit_price = float(input("Enter Unit Price (Rs): "))

# # Calculations
# total_price = quantity * unit_price

# # Get today's date
# today = datetime.today().strftime("%d/%m/%Y")

# # Display invoice
# print("\n" + "="*70)
# print(f"{company_name}")
# print(f"{company_address}")
# print(f"{phone_number}")
# print(f"{website}")
# print("="*70)
# print("\nINVOICE")
# print(f"Submitted on: {today}\n")
# print(f"Invoice for: {invoice_for}")
# print(f"Payable to: {payable_to}")
# print(f"Invoice #: {invoice_no}")
# print("-" * 70)
# print(f"{'Description':<25}{'Delivery Date':<15}{'Qty (M/TON)':<15}{'Unit Price':<15}{'Total Price':<15}")
# print("-" * 70)
# print(f"Coal ({vehicle_number})  {delivery_date:<15}{quantity:<15.3f}Rs{unit_price:<12,.0f}Rs{total_price:,.0f}")
# print("-" * 70)
# print(f"{'':<65}Rs{total_price:,.0f}")
# print("\nAmount in Words: ", end="")

# # Function to convert amount to words
# try:
#     from num2words import num2words
#     print(num2words(total_price, to='currency', lang='en_IN').replace('euro', 'Rupees').title())
# except ImportError:
#     print("(Install 'num2words' for full amount in words)")

# print("=" * 70)


# Invoice Generator for A.T Commodities (Chatgpt Version)(with pdf future)
#----------------------------------------------------------------

# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from datetime import datetime

# # Function to convert number to words
# try:
#     from num2words import num2words
# except ImportError:
#     num2words = None

# # ==== Static Data ====
# company_name = "A.T COMMODITIES"
# company_address = "C-2 WESTLAND TRADE CENTER\nSHAHEED E MILLAT ROAD, KARACHI"
# phone_number = "021-34381222"
# website = "www.atcommodities.pk"
# payable_to = "A.T COMMODITIES"
# invoice_for = "Mr. Talha Niazi Sb\nNiazi Bricks"

# # ==== User Inputs ====
# invoice_no = input("Invoice No: ")
# delivery_date = input("Delivery Date (e.g., 29-May-2025): ")
# vehicle_number = input("Vehicle Number: ")
# quantity = float(input("Quantity (M/TON): "))
# unit_price = float(input("Unit Price (Rs): "))
# total_price = quantity * unit_price
# today = datetime.today().strftime("%d/%m/%Y")

# # ==== File Name ====
# file_name = f"Invoice_{invoice_no}.pdf"

# # ==== Create PDF ====
# c = canvas.Canvas(file_name, pagesize=A4)
# width, height = A4
# y = height - 50

# # ==== Header ====
# c.setFont("Helvetica-Bold", 16)
# c.drawString(50, y, company_name)
# y -= 20
# c.setFont("Helvetica", 10)
# for line in company_address.split('\n'):
#     c.drawString(50, y, line)
#     y -= 15
# c.drawString(50, y, f"Phone: {phone_number}")
# y -= 15
# c.drawString(50, y, f"Website: {website}")
# y -= 30

# # ==== Invoice Title ====
# c.setFont("Helvetica-Bold", 14)
# c.drawString(50, y, "INVOICE")
# c.setFont("Helvetica", 10)
# c.drawString(350, y, f"Submitted on: {today}")
# y -= 20

# # ==== Invoice Details ====
# c.drawString(50, y, f"Invoice for: {invoice_for.splitlines()[0]}")
# y -= 15
# c.drawString(50, y, f"{invoice_for.splitlines()[1]}")
# c.drawString(350, y + 15, f"Payable to: {payable_to}")
# c.drawString(350, y, f"Invoice #: {invoice_no}")
# y -= 30

# # ==== Table Header ====
# c.setFont("Helvetica-Bold", 10)
# c.drawString(50, y, "Description")
# c.drawString(200, y, "Delivery Date")
# c.drawString(300, y, "Qty (M/TON)")
# c.drawString(390, y, "Unit Price")
# c.drawString(470, y, "Total Price")
# y -= 15
# c.line(50, y, 550, y)
# y -= 15

# # ==== Table Content ====
# c.setFont("Helvetica", 10)
# description = f"Coal ({vehicle_number})"
# c.drawString(50, y, description)
# c.drawString(200, y, delivery_date)
# c.drawString(300, y, f"{quantity:.3f}")
# c.drawString(390, y, f"Rs{unit_price:,.0f}")
# c.drawString(470, y, f"Rs{total_price:,.0f}")
# y -= 25

# # ==== Total ====
# c.line(390, y, 550, y)
# y -= 15
# c.setFont("Helvetica-Bold", 11)
# c.drawString(390, y, "Total:")
# c.drawString(470, y, f"Rs{total_price:,.0f}")
# y -= 30

# # ==== Amount in Words ====
# c.setFont("Helvetica", 10)
# if num2words:
#     words = num2words(total_price, to='currency', lang='en_IN').replace("euro", "rupees").title()
#     c.drawString(50, y, f"Amount in Words: {words}")
# else:
#     c.drawString(50, y, f"Amount in Words: (Install num2words to show words)")

# # ==== Save PDF ====
# c.save()

# print(f"✅ Invoice saved successfully as: {file_name}")



# Invoice Generator for A.T Commodities (Deepseek Version)(with pdf future)
#----------------------------------------------------------------


import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from num2words import num2words

# Static company information
COMPANY_NAME = "A.T COMMODITIES"
ADDRESS = "C-2 WESTLAND TRADE CENTER, SHAHEED E MILLAT ROAD, KARACHI"
PHONE = "021-34381222"
WEBSITE = "www.atcommodities.pk"
CUSTOMER = "Mr. Talha Niazi Sb - Niazi Bricks"
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
    
    # Format the invoice details
    invoice_text = f"""
{COMPANY_NAME}
{ADDRESS}
{PHONE}
{WEBSITE}

{'Invoice':^60}
{'Submitted on: ' + datetime.datetime.now().strftime('%d/%m/%Y'):^60}

{'-'*60}
| {'Invoice for':<30} | {'Payable to':<20} | {'Invoice #':<8} |
| {CUSTOMER:<30} | {PAYABLE_TO:<20} | {invoice_no:<8} |
{'-'*60}

| {'Description':<20} | {'Delivery Date':<15} | {'Qty (M/TON)':>12} | {'Unit price':>12} | {'Total price':>12} |
| {'Coal (' + vehicle_no + ')':<20} | {delivery_date:<15} | {quantity:>12.3f} | {'Rs' + f'{unit_price:,.0f}':>12} | {'Rs' + f'{total:,.0f}':>12} |
{'-'*60}

Notes:
Rs{total:,.0f}

{amount_in_words}
"""
    print(invoice_text)

def generate_pdf_invoice(invoice_no, delivery_date, vehicle_no, quantity, unit_price, total):
    """Generate a PDF invoice using reportlab."""
    amount_in_words = num2words(total, lang='en_IN').title().replace("And", "") + " Rupees Only"
    file_name = f"Invoice_{invoice_no}.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    style_center = ParagraphStyle(name='Center', alignment=1, parent=styles['Normal'])
    style_right = ParagraphStyle(name='Right', alignment=2, parent=styles['Normal'])
    
    # Company Information
    elements.append(Paragraph(COMPANY_NAME, styles['Heading1']))
    elements.append(Paragraph(ADDRESS, styles['Normal']))
    elements.append(Paragraph(f"Phone: {PHONE} &nbsp;&nbsp; Website: {WEBSITE}", styles['Normal']))
    elements.append(Spacer(1, 20))
    
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
    elements.append(Paragraph(f"Notes:", styles['Normal']))
    elements.append(Paragraph(f"Rs{total:,.0f}", styles['Normal']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(amount_in_words, styles['Normal']))
    
    # Build PDF
    doc.build(elements)
    print(f"PDF invoice saved as '{file_name}'")

def main():
    # Collect user inputs
    invoice_no, delivery_date, vehicle_no, quantity, unit_price = get_user_inputs()
    total = quantity * unit_price
    
    # Generate text invoice
    generate_text_invoice(invoice_no, delivery_date, vehicle_no, quantity, unit_price, total)
    
    # Generate PDF invoice
    generate_pdf_invoice(invoice_no, delivery_date, vehicle_no, quantity, unit_price, total)

if __name__ == "__main__":
    main()
