from flat import Bill, Flatmate
from reports import PdfReport

name1 = input('What is your name? ')
BillAmount = float(input(f'Hey {name1}, please enter the bill amount: '))
period = input('What is the bill period? (for example "April 2021"): ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house during the bill period? '))

name2 = input('What is the name of the other flatmate? ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house during the bill period? '))

TheBill = Bill(amount=BillAmount, period=period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f'{flatmate1.name} pays: ', flatmate1.pays(TheBill, flatmate2))
print(f'{flatmate2.name} pays: ', flatmate2.pays(TheBill, flatmate1))

pdf_report = PdfReport(filename=f'{TheBill.period} .pdf')
pdf_report.generate(flatmate1, flatmate2, bill=TheBill)