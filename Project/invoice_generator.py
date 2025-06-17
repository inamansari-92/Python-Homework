from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime
import os

# Fixed company information
COMPANY_NAME = "A.T COMMODITIES"
ADDRESS = "C-2 WESTLAND TRADE CENTER, SHAHEED E MILLAT ROAD, KARACHI"
PHONE = "021-34381222"
WEBSITE = "www.atcommodities.pk"

def generate_invoice():
    # Get user inputs
    invoice_number = input("Enter Invoice Number: ")
    delivery_date = input("Enter Delivery Date (DD-MMM-YYYY): ")
    vehicle_number = input("Enter Vehicle Number: ")
    quantity = float(input("Enter Quantity (M/TON): "))
    unit_price = float(input("Enter Unit Price (Rs): "))
    
    # Calculate total
    total_price = quantity * unit_price
    
    # Print text invoice
    print("\n" + "="*60)
    print(f"{COMPANY_NAME:^60}")
    print(f"{ADDRESS:^60}")
    print(f"Phone: {PHONE:^50}")
    print(f"Website: {WEBSITE:^50}")
    print("="*60)
    print(f"Invoice for: Mr. Talha Niazi Sb - Niazi Bricks")
    print(f"Payable to: {COMPANY_NAME}")
    print(f"Invoice #: {invoice_number}")
    print("-"*60)
    print(f"{'Description':<20}{'Delivery Date':<15}{'Qty (M/TON)':>12}{'Unit Price':>12}{'Total Price':>15}")
    print(f"{'Coal (' + vehicle_number + ')':<20}{delivery_date:<15}{quantity:>12.3f}{unit_price:>12,.2f}{total_price:>15,.2f}")
    print("-"*60)
    print(f"Total: Rs{total_price:,.2f}")
    print("="*60)
    print(f"\nAmount in Words: {number_to_words(total_price)} Rupees Only\n")
    
    # Generate PDF
    generate_pdf(invoice_number, delivery_date, vehicle_number, quantity, unit_price, total_price)

def number_to_words(num):
    """Convert number to words (simplified version)"""
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    if num == 0:
        return "Zero"
    
    def convert_below_thousand(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[int(n)]
        elif n < 20:
            return teens[int(n)-10]
        elif n < 100:
            return tens[int(n//10)] + (" " + units[int(n%10)] if n%10 !=0 else "")
        else:
            return units[int(n//100)] + " Hundred" + (" and " + convert_below_thousand(n%100) if n%100 !=0 else "")
    
    # Main conversion logic
    result = ""
    if num >= 1000000:
        millions = num // 1000000
        result += convert_below_thousand(millions) + " Million "
        num %= 1000000
    if num >= 1000:
        thousands = num // 1000
        result += convert_below_thousand(thousands) + " Thousand "
        num %= 1000
    if num > 0:
        result += convert_below_thousand(num)
    
    return result.strip()

def generate_pdf(invoice_number, delivery_date, vehicle_number, quantity, unit_price, total_price):
    # Create PDF document
    filename = f"Invoice_{invoice_number}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    # Create story
    story = []
    styles = getSampleStyleSheet()
    
    # Company header
    company_info = [
        [COMPANY_NAME],
        [ADDRESS],
        [f"Phone: {PHONE}"],
        [f"Website: {WEBSITE}"]
    ]
    
    # Invoice details
    invoice_details = [
        ["Invoice for", "Mr. Talha Niazi Sb - Niazi Bricks"],
        ["Payable to", COMPANY_NAME],
        ["Invoice #", invoice_number]
    ]
    
    # Item table
    item_data = [
        ["Description", "Delivery Date", "Qty (M/TON)", "Unit price", "Total price"],
        [f"Coal ({vehicle_number})", delivery_date, f"{quantity:.3f}", f"Rs{unit_price:,.2f}", f"Rs{total_price:,.2f}"]
    ]
    
    # Summary
    summary = [
        ["Total Amount:", f"Rs{total_price:,.2f}"],
        ["Amount in Words:", f"{number_to_words(total_price)} Rupees Only"]
    ]
    
    # Create tables
    company_table = Table(company_info)
    invoice_table = Table(invoice_details)
    item_table = Table(item_data)
    summary_table = Table(summary, colWidths=[300, 200])
    
    # Apply styles
    company_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,0), 14),
        ('BOTTOMPADDING', (0,0), (0,0), 12),
    ]))
    
    invoice_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTSIZE', (0,0), (-1,-1), 10),
    ]))
    
    item_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('ALIGN', (2,1), (4,1), 'RIGHT'),
    ]))
    
    summary_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (0,0), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
        ('LINEABOVE', (0,1), (-1,1), 1, colors.black),
    ]))
    
    # Add elements to story
    story.append(company_table)
    story.append(Spacer(1, 0.25*inch))
    story.append(invoice_table)
    story.append(Spacer(1, 0.25*inch))
    story.append(item_table)
    story.append(Spacer(1, 0.25*inch))
    story.append(summary_table)
    
    # Build PDF
    doc.build(story)
    print(f"\nPDF invoice generated: {os.path.abspath(filename)}")

if __name__ == "__main__":
    generate_invoice()