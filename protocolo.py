from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors



class Protocolo:
    def __init__(self, ano, unidadegestora, numeracao, assunto, tipoprocesso, locprocesso, dataprotocolo, secaoprotocolo):
        self.ano = ano
        self.unidadegestora = unidadegestora
        self.numeracao = numeracao
        self.assunto = assunto
        self.tipoprocesso = tipoprocesso
        self.locprocesso = locprocesso
        self.locprocesso = locprocesso
        self.dataprotocolo = dataprotocolo
        self.secaoprotocolo = secaoprotocolo
    
    def desenharRef(self, pdf):
        pdf.drawString(100,810, 'x100')
        pdf.drawString(200,810, 'x200')
        pdf.drawString(300,810, 'x300')
        pdf.drawString(400,810, 'x400')
        pdf.drawString(500,810, 'x500')
        
        pdf.drawString(10,100, 'y100')
        pdf.drawString(10,200, 'y200')
        pdf.drawString(10,300, 'y300')
        pdf.drawString(10,400, 'y400')
        pdf.drawString(10,500, 'y500')
        pdf.drawString(10,600, '6100')
        pdf.drawString(10,700, '7100')
        pdf.drawString(10,800, 'y800')
        
    def cria_pdf(self):
        # w, h = A4
        # impressao = canvas.Canvas(f"{self.ano}.pdf", pagesize=A4)
        # impressao.setFont("Times-Roman", 18)
        # impressao.drawString(50, h - 50, "Hello, world!")
        # impressao.drawString(72, h-72, self.assunto)
        
        # impressao.showPage()
        
        
        # impressao.save()
        impre = SimpleDocTemplate('assets/protocolo.pdf')
        # self.desenharRef(impre)
        # sample_style_sheet = getSampleStyleSheet()
        styles = getSampleStyleSheet()
        headline_style = styles["Heading2"]
        headline_style.alignment = TA_CENTER
        headline_style.fontSize = 16
        headline_style.spaceAfter = 20
        
        cabecalho_style = styles["Heading1"]
        cabecalho_style.alignment = TA_CENTER
        cabecalho_style.fontSize = 48
        cabecalho_style.spaceAfter = 50
        
        assinatura_style = styles["BodyText"]
        assinatura_style.alignment = TA_CENTER
        assinatura_style.spaceBefore = 30
        
        paragraph_style = styles["BodyText"]
        paragraph_style.alignment = TA_LEFT
        paragraph_style.fontSize = 12
        # paragraph_style.spaceBefore = 30
        
        # if you want to see all the sample styles, this prints them
        # sample_style_sheet.list()
        espaco = Spacer(width=0, height=5*cm) 
        
        flowables = []
        
        cabecalho = Paragraph("Conformidade", cabecalho_style)
        paragraph_1 = Paragraph("PROTOCOLO DE RECEBIMENTO DE DOCUMENTOS", headline_style)
        paragraph_2 = Paragraph(
            "Data do Recebimento:  " + self.dataprotocolo,
            paragraph_style
        )
        paragraph_3 = Paragraph(
            "Documentos Recebidos:  Processo nr " + self.numeracao + " - " + self.tipoprocesso + " sobre " + self.assunto,
            paragraph_style
        )
        paragraph_4 = Paragraph(
            "Seção:   " + self.secaoprotocolo,
            paragraph_style
        )
        
        assinatura = Paragraph(
            "_________________________", assinatura_style
        )
        flowables.append(cabecalho)
        flowables.append(paragraph_1)
        flowables.append(paragraph_2)
        flowables.append(paragraph_3)
        flowables.append(paragraph_4)
        flowables.append(assinatura)
        
        flowables.append(espaco)
        
        flowables.append(cabecalho)
        flowables.append(paragraph_1)
        flowables.append(paragraph_2)
        flowables.append(paragraph_3)
        flowables.append(paragraph_4)
        flowables.append(assinatura)
        
        impre.build(flowables)