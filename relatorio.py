from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.graphics import shapes

import os
import json

os.makedirs("Protocolo", exist_ok=True)



class Relatorio:
    def __init__(self, query, categoria, tipodepesquisa):
        self.query = query
        self.categoria = categoria
        self.tipodepesquisa = tipodepesquisa
        
    def cria_pdf(self):
        imprerela = SimpleDocTemplate('Protocolo/relatorio.pdf',
                        pagesize=A4,
                        rightMargin=1.5*cm,
                        leftMargin=1*cm,
                        topMargin=1*cm,
                        bottomMargin=1.5*cm)
        
        styles = getSampleStyleSheet()
        
        headline_style = styles["Heading2"]
        headline_style.alignment = TA_CENTER
        headline_style.fontSize = 16
        headline_style.spaceAfter = 10
        
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
        
        
        espaco = Spacer(width=0, height=1.5*cm) 
        
        flowables = []
        
        cabecalho = Paragraph("Conformidade - HGes", cabecalho_style)
        paragraph_1 = Paragraph("RELATÓRIO DE DOCUMENTOS DA CONFORMIDADE", headline_style)
        paragraph_0 = Paragraph(self.categoria.upper() + " '"+ self.tipodepesquisa +"'", headline_style)

        # cabecalho_string = "Conformidade - HGeS"
        # paragraph_1_string = "RELATÓRIO DE DOCUMENTOS DA CONFORMIDADE"
        # paragraph_0_string = self.categoria.upper() + " '"+ self.tipodepesquisa +"' "
        # cabecalho_tabela = Paragraph("--------------------------------------------------------------------", paragraph_style)

        # draw = shapes.Drawing(520, 200)
        # draw.add(shapes.Rect(0, 100, 520, 100, fillColor=None))   
        # draw.add(shapes.String(150,170, cabecalho_string, fontSize=30, fillColor=colors.black)) 
        # draw.add(shapes.String(12,140, paragraph_1_string, fontSize=20, fillColor=colors.black)) 
        # # draw.add(shapes.String((520-len(paragraph_0_string))/len(paragraph_0_string),110, paragraph_0_string, fontSize=20, fillColor=colors.black)) 
        # # print((520/len(cabecalho_string)))
        # # print((520-len(paragraph_1_string))/len(paragraph_1_string))
        # # print((520-len(paragraph_0_string))/len(paragraph_0_string))
        
        # flowables.append(draw)
        
        flowables.append(cabecalho)
        flowables.append(paragraph_1)
        flowables.append(paragraph_0)
        
        # options = list()
        # options.append([Paragraph("<strong>ANO</strong>", paragraph_style), Paragraph("<strong>ASSUNTO</strong>", paragraph_style), Paragraph("<strong>UG</strong>", paragraph_style), Paragraph("<strong>NUMERAÇÃO</strong>", paragraph_style)])

        # for i,row in enumerate(self.query):
        #     options.append([Paragraph(row.ano,paragraph_style), Paragraph(row.assunto, paragraph_style), Paragraph(row.unidadegestora,paragraph_style), Paragraph(row.numeracao, paragraph_style)])
        
        # tabela=Table(options,colWidths=4*cm, rowHeights=1.5*cm,style=[
        #     ('GRID',(0,0),(-1,-1),0.5,colors.grey),
        #         ])
    
        # flowables.append(tabela)
        # flowables.append(espaco)
        
        # flowables.append(cabecalho_tabela)

        for index, doc in enumerate(self.query):      
            paragraph_2 = Paragraph(
                str(index+1) + ") <strong>Ano:</strong> "+ doc.ano + " | <strong>UG</strong>: " + doc.unidadegestora + " | <strong>Nr:</strong> " + doc.numeracao + " | <strong>Assunto:</strong> " + doc.assunto +" | <strong>Processo:</strong> " + doc.tipoprocesso +" | <strong>Localização:</strong> " + doc.locprocesso,
                paragraph_style
            )
            flowables.append(paragraph_2)
                    
        imprerela.build(flowables)