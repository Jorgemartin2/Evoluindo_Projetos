from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

class Reports():
    def print_customers(self):
        webbrowser.open("Clientes.pdf")

    def generate_reports(self):
        self.cvs=canvas.Canvas("Clientes.pdf")

        self.id_report=self.entry_id.get()
        self.name_report=self.entry_name.get()
        self.birth_report=self.entry_birth.get()
        self.telephone_report=self.entry_telephone.get()
        self.cel_report=self.entry_cel.get()
        self.email_report=self.entry_email.get()
        self.address_report=self.entry_address.get()
        self.number_report=self.entry_number.get()
        self.cep_report=self.entry_cep.get()
        self.city_report=self.entry_city.get()
        self.uf_report=self.entry_uf.get()
        self.complement_report=self.entry_complement.get()
        self.obs_report=self.entry_obs.get()

        self.cvs.setFont("Helvetica-Bold", 24)
        self.cvs.drawString(200, 790, 'Ficha do Cliente')

        self.cvs.setFont("Helvetica-Bold", 18)
        self.cvs.drawString(50, 700, 'ID: ')
        self.cvs.drawString(50, 670, 'NOME: ')
        self.cvs.drawString(50, 640, 'ANIVERSÁRIO: ')
        self.cvs.drawString(50, 610, 'TELEFONE: ')
        self.cvs.drawString(50, 580, 'CELULAR: ')
        self.cvs.drawString(50, 550, 'EMAIL: ')
        self.cvs.drawString(50, 520, 'ENDEREÇO: ')
        self.cvs.drawString(50, 490, 'NÚMERO: ')
        self.cvs.drawString(50, 460, 'CEP: ')
        self.cvs.drawString(50, 430, 'CIDADE: ')
        self.cvs.drawString(50, 400, 'UF: ')
        self.cvs.drawString(50, 370, 'COMPLEMENTO: ')
        self.cvs.drawString(50, 340, 'OBSERVAÇÃO: ')

        self.cvs.setFont("Helvetica", 18)
        self.cvs.drawString(80, 700, self.id_report)
        self.cvs.drawString(115, 670, self.name_report)
        self.cvs.drawString(185, 640, self.birth_report)
        self.cvs.drawString(155, 610, self.telephone_report)
        self.cvs.drawString(145, 580, self.cel_report)
        self.cvs.drawString(115, 550, self.email_report)
        self.cvs.drawString(165, 520, self.address_report)
        self.cvs.drawString(140, 490, self.number_report)
        self.cvs.drawString(95, 460, self.cep_report)
        self.cvs.drawString(130, 430, self.city_report)
        self.cvs.drawString(85, 400, self.uf_report)
        self.cvs.drawString(205, 370, self.complement_report)
        self.cvs.drawString(190, 340, self.obs_report)

        self.cvs.showPage()
        self.cvs.save()
        self.print_customers()