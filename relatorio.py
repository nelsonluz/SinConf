from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors

import os

os.makedirs("Protocolo", exist_ok=True)



class Relatorio:
    def __init__(self, query, categoria, tipodepesquisa):
        self.query = query
        self.categoria = categoria
        self.tipodepesquisa = tipodepesquisa
        # self.unidadegestora = unidadegestora
        # self.numeracao = numeracao
        # self.assunto = assunto
        # self.tipoprocesso = tipoprocesso
        # self.locprocesso = locprocesso
        # self.locprocesso = locprocesso
        # self.dataprotocolo = dataprotocolo
        # self.secaoprotocolo = secaoprotocolo
    
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
        imprerela = SimpleDocTemplate('Protocolo/relatorio.pdf')
        # self.desenharRef(impre)
        # sample_style_sheet = getSampleStyleSheet()
        styles = getSampleStyleSheet()
        headline_style = styles["Heading2"]
        headline_style.alignment = TA_CENTER
        headline_style.fontSize = 16
        # headline_style.spaceAfter = 10
        
        cabecalho_style = styles["Heading1"]
        cabecalho_style.alignment = TA_CENTER
        cabecalho_style.fontSize = 30
        cabecalho_style.spaceAfter = 10
        
        assinatura_style = styles["BodyText"]
        assinatura_style.alignment = TA_CENTER
        assinatura_style.spaceBefore = 30
        
        paragraph_style = styles["Normal"]
        paragraph_style.alignment = TA_JUSTIFY
        paragraph_style.fontSize = 10
        paragraph_style.spaceBefore = 5
        
        
        # if you want to see all the sample styles, this prints them
        # sample_style_sheet.list()
        espaco = Spacer(width=0, height=1.5*cm) 
        
        flowables = []
        cabecalho = Paragraph("Conformidade - HGes", cabecalho_style)
        paragraph_1 = Paragraph("RELATÓRIO DE DOCUMENTOS DA CONFORMIDADE", headline_style)
        paragraph_0 = Paragraph(self.categoria, headline_style)
        # cabecalho_tabela = Paragraph("--------------------------------------------------------------------", paragraph_style)
        flowables.append(cabecalho)
        flowables.append(paragraph_1)
        flowables.append(paragraph_0)
        
        # flowables.append(espaco)
        
        # flowables.append(cabecalho_tabela)
        for index, doc in enumerate(self.query):
            print(f"Relatorio: {doc.ano}")
            # self.numeracao = numeracao
            # self.assunto = assunto
            # self.tipoprocesso = tipoprocesso
            # self.locprocesso = locprocesso
            # self.locprocesso = locprocesso
            # self.dataprotocolo = dataprotocolo
            # self.secaoprotocolo = secaoprotocolo        
            paragraph_2 = Paragraph(
                # str(index+1) + ") "+ doc.ano + " | " + doc.unidadegestora + " | " + doc.numeracao + " | " + doc.assunto +" | " + doc.tipoprocesso,
                # paragraph_style
                # str(index+1) + ") <strong>Ano:</strong> "+ doc.ano + " | UG: " + doc.unidadegestora + " | Nr: " + doc.numeracao + " | Ass: " + doc.assunto +" | Proc: " + doc.tipoprocesso,
                # paragraph_style
                str(index+1) + ") <strong>Ano:</strong> "+ doc.ano + " | <strong>UG</strong>: " + doc.unidadegestora + " | <strong>Nr:</strong> " + doc.numeracao + " | <strong>Assunto:</strong> " + doc.assunto +" | <strong>Processo:</strong> " + doc.tipoprocesso,
                paragraph_style
            )
            flowables.append(paragraph_2)
            
        # paragraph_3 = Paragraph(
        #     "Documentos Recebidos:  Processo nr " + self.numeracao + " - " + self.tipoprocesso + " sobre " + self.assunto,
        #     paragraph_style
        # )
        # paragraph_4 = Paragraph(
        #     "Seção:   " + self.secaoprotocolo,
        #     paragraph_style
        # )
        
        # assinatura = Paragraph(
        #     "_________________________", assinatura_style
        # )
        # flowables.append(cabecalho)
        # flowables.append(paragraph_1)
        # flowables.append(paragraph_2)
        # flowables.append(paragraph_3)
        # flowables.append(paragraph_4)
        # flowables.append(assinatura)
        
        # flowables.append(espaco)
        
        # flowables.append(cabecalho)
        # flowables.append(paragraph_1)
        # flowables.append(paragraph_2)
        # flowables.append(paragraph_3)
        # flowables.append(paragraph_4)
        # flowables.append(assinatura)
        
        imprerela.build(flowables)