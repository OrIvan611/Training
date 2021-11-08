import webbrowser
from fpdf import FPDF
import os

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 3))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 3))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icone
        pdf.image('files/house.png', w=40, h=40)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # insert period label and period
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt='Period: ', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #insert name and due amount of the flatemate1
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name , border=0)
        pdf.cell(w=100, h=25, txt=flatmate1_pay, border=0, ln=1)

        #insert name and due amount of the flatemate2
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=flatmate2.name , border=0)
        pdf.cell(w=100, h=25, txt=flatmate2_pay, border=0, ln=1)

        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)


