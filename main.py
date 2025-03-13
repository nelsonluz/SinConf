from operator import contains
from re import I
import flet as ft
from flet.core.grid_view import ScrollableControl
from dbdocument import Document
from protocolo import Protocolo
from relatorio import Relatorio


def main(page: ft.Page):
    cor = ft.colors.BLACK54
    page.title = "Sistema de Controle de Documentos"
    
    page.window.min_width = 1400
    page.window.min_height = 900
    page.window.maximized = True

    page.theme_mode=ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary=ft.colors.BLACK54),
    )
    
    def sair(e):
        page.window.close()
    
    def zeravariaveis():
        ano.value = ""
        unidadegestoradown.value = ""
        numeracao.value = ""
        assunto.value = ""
        tipoprocesso.value = ""
        locprocesso.value = ""
        page.update()
    
    def zeratualizar():
        id_atualizar.value = ""
        ano_atualizar.value = ""
        unidadegestoradown_atualizar.value = ""
        numeracao_atualizar.value = ""
        assunto_atualizar.value = ""
        tipoprocesso_atualizar.value = ""
        locprocesso_atualizar.value = ""
        dataprotocolo_atualizar.value=""
        secaoprotocolo_atualizar.value= ""
        
        atualizar_conteiner.visible = False
        radio_pesquisa.visible = True
        campo_pesquisa.visible = True
        
        campo_pesquisa.update()
        radio_pesquisa.update()
        page.update()
    
    def zerarimprerela():
        categoriaimpressao.value = "" 
        pesquisa_impressao_relatorio.value = ""
        page.update()
        
    
    def preencher_campos(e):
        atualizar_conteiner.visible=True
        radio_pesquisa.visible=False
        campo_pesquisa.visible=False
        radio_pesquisa.update()
        campo_pesquisa.update()
        dooc=Document.get(Document.id==int(e.control.cells[0].content.value))
        id_atualizar.value=dooc.id
        ano_atualizar.value=dooc.ano
        unidadegestoradown_atualizar.value = dooc.unidadegestora 
        numeracao_atualizar.value = dooc.numeracao
        assunto_atualizar.value = dooc.assunto
        tipoprocesso_atualizar.value = dooc.tipoprocesso
        locprocesso_atualizar.value = dooc.locprocesso
        dataprotocolo_atualizar.value = dooc.dataprotocolo
        secaoprotocolo_atualizar.value = dooc.secaoprotocolo
        atualizar_conteiner.update()
    
    def cancelar(e):
        zeratualizar()
        
    def cadastrar(e):
        print(f"Cadastro {e}")
        print(f"ano {ano.value}")
        Document.create(ano=ano.value, unidadegestora=unidadegestoradown.value, numeracao=numeracao.value, assunto=assunto.value,tipoprocesso=tipoprocesso.value, locprocesso=locprocesso.value, dataprotocolo="", secaoprotocolo="")
        zeravariaveis()
        
    def imprimir(e):
        printed = Protocolo(ano_atualizar.value,unidadegestoradown_atualizar.value, numeracao_atualizar.value, assunto_atualizar.value, tipoprocesso_atualizar.value, locprocesso_atualizar.value, dataprotocolo_atualizar.value, secaoprotocolo_atualizar.value)
        printed.cria_pdf()
        print(f"Funcao Imprimir: {ano_atualizar.value}, {unidadegestoradown_atualizar.value}, {numeracao_atualizar.value}, {assunto_atualizar.value}, {tipoprocesso_atualizar.value}, {locprocesso_atualizar.value}, {dataprotocolo_atualizar.value}, {secaoprotocolo_atualizar.value} ")
        zeratualizar()
    
    def impressao_relatório(e):
        print(f"impressao relatorio {categoriaimpressao.value} ")
        match categoriaimpressao.value:
            case "ano":
                query = Document.select().where(Document.ano.contains(pesquisa_impressao_relatorio.value))
            case "assunto":
                query = Document.select().where(Document.assunto.contains(pesquisa_impressao_relatorio.value)).order_by(Document.ano.asc())
            case _:
                categoriaimpressao.value =  "arquivos"
                pesquisa_impressao_relatorio.value = "Completo"
                query = Document.select().order_by(Document.ano.asc())

        relatorio = Relatorio(query, categoriaimpressao.value, pesquisa_impressao_relatorio.value)
        relatorio.cria_pdf()
                
        zerarimprerela()
        
        
    
    # def relatorio(query_relatorio):
    #     for doc in query_relatorio:
    #         print(f"assunto: {doc.assunto}, ano: {doc.ano}")
        
    def criar_pesquisa(e):
        saida_radio.value = e.control.value
        page.update()
                
    def pesquisar(e):
        if saida_radio.value == "ano":
            preencher_datatable(Document.select().where(
                Document.ano.contains(e.control.value)
                )
            )
        elif saida_radio.value == "assunto":
            preencher_datatable(Document.select().where(
                Document.assunto.contains(e.control.value)
                )
            )
        elif saida_radio.value == "processo":
            preencher_datatable(Document.select().where(
                Document.tipoprocesso.contains(e.control.value)
                )
            )
        elif saida_radio.value == "UG":
            preencher_datatable(Document.select().where(
                Document.unidadegestora.contains(e.control.value)
                )
            )
        elif saida_radio.value == "locprocesso":
            preencher_datatable(Document.select().where(
                Document.locprocesso.contains(e.control.value)
                )
            )
        elif saida_radio.value == "numeracao":
            preencher_datatable(Document.select().where(
                Document.numeracao.contains(e.control.value)
                )
            )
       
    
    def apagar(e):
        atualizacao = Document.delete().where(Document.id==id_atualizar.value)
        print(f"funcao apagar: {atualizacao}")
        
        atualizacao.execute()
        
        zeratualizar()
        campo_pesquisa.value = ""
        preencher_datatable(Document.select())
        pesquisa.update()
        print(f"apagar {e}")
    
    def atualizar(e):
        atualizacao = Document.update({
            Document.ano:ano_atualizar.value,
            Document.unidadegestora:unidadegestoradown_atualizar.value,
            Document.numeracao:numeracao_atualizar.value,
            Document.assunto:assunto_atualizar.value,
            Document.tipoprocesso:tipoprocesso_atualizar.value,
            Document.locprocesso:locprocesso_atualizar.value,
            Document.dataprotocolo:dataprotocolo_atualizar.value,
            Document.secaoprotocolo:secaoprotocolo_atualizar.value,
            }).where(Document.id==id_atualizar.value)
        print(f"funcao atualizar: {atualizacao}")
        
        atualizacao.execute()
        
        zeratualizar()
        campo_pesquisa.value=""
        preencher_datatable(Document.select())
        pesquisa.update()
    
    def preencher_datatable(query):
        cores=[ft.colors.GREEN_50, ft.colors.BLACK45]
        pesquisa.rows.clear()
        for i, doc in enumerate(query, 1):
            pesquisa.rows.append(
                
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(doc.id), visible=False), 
                    ft.DataCell(ft.Text(doc.ano, color=cor, size=15,  on_tap=preencher_campos,)), 
                    ft.DataCell(ft.Text(doc.unidadegestora, color=cor, size=15)), 
                    ft.DataCell(ft.Text(doc.numeracao, color=cor, size=15)),
                    ft.DataCell(ft.Container(content=ft.Column(controls=[ft.Text(doc.assunto, color=cor, size=15),], scroll=ft.ScrollMode.ALWAYS), width=200)),  
                    ft.DataCell(ft.Container(content=ft.Column(controls=[ft.Text(doc.tipoprocesso, color=cor, size=15),], scroll=ft.ScrollMode.ALWAYS), width=200)), 
                    ft.DataCell(ft.Container(content=ft.Column(controls=[ft.Text(doc.locprocesso, color=cor, size=15),], scroll=ft.ScrollMode.ALWAYS), width=150)),
                    ft.DataCell(ft.Text(doc.dataprotocolo, color=cor, size=15)),
                    ft.DataCell(ft.Text(doc.secaoprotocolo, color=cor, size=15)),
                    ],
                    color=cores[i%2],
                    on_select_changed=preencher_campos,
                    )
            )
        page.update()
    
    def set_screen(e):
        principal.content=screen_lista[e.control.selected_index]
        if e.control.selected_index == 1:
            preencher_datatable(Document.select())
        page.update()
    
    rail = ft.NavigationRail(
        bgcolor=ft.colors.BLACK,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.Icons.DOCUMENT_SCANNER_OUTLINED, text="CONTROLE \nDOCUMENTOS"),
        group_alignment=0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.BOOK_OUTLINED,
                selected_icon=ft.Icons.BOOK,
                label_content=ft.Text("Cadastrar", color=ft.Colors.WHITE),
                
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.NEWSPAPER_OUTLINED,
                selected_icon=ft.Icons.NEWSPAPER,
                label_content=ft.Text("Relatório", color=ft.Colors.WHITE),                
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PRINT_OUTLINED,
                selected_icon=ft.Icons.PRINT,
                label_content=ft.Text("Impressão", color=ft.Colors.WHITE),                
            ),
        ],
        on_change=set_screen,  
    )
    
    # def fechardlg(e):
    #     page.close(dlg_modal)
    
    titulo = "Sistema de Controle de Documentos"
    subtitulo = "CONFORMIDADE"
    titulo_conteiner = ft.Container(
        content = ft.Text(titulo,
                    size=20,
                    color=cor,
                    weight="bold",
                ),
        bgcolor = ft.Colors.BLACK12,
        border_radius = ft.border_radius.all(25),
        padding = 15,
    )
    subtitulo_conteiner = ft.Container(
        content = ft.Text(subtitulo,
                    size=20,
                    color=cor,
                    weight="bold",
        ),
        margin=ft.margin.only(left=120),
        padding= 15,
        bgcolor = ft.Colors.BLACK12,
        border_radius = ft.border_radius.all(25),
    )
    titulo_processo = ft.Text(
        "Controle de Processos arquivado na Conformidade",
        color=cor,
        size=25,
        weight="bold",
    )
 
    cabecalho = ft.Container(
        alignment=ft.alignment.center,
        padding= 5,
        bgcolor = ft.Colors.BLACK12,
        border_radius = ft.border_radius.all(25),
        content=ft.Text("HOSPITAL GERAL DE SALVADOR - HGeS", color=cor, size=20, weight="bold"),
    )
 
    
    ano = ft.TextField(label="Digite o Ano do Processo",  color=cor)
    unidadegestoradown = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("160039"),
            ft.dropdown.Option("167039"),
        ]
    )
    numeracao = ft.TextField(label="Digite o número do Processo", color=cor, width=600)
    assunto = ft.TextField(label="Digite o assunto do processo", color=cor, width=600)
    tipoprocesso = ft.TextField(label="Digite o tipo do processo", color=cor, width=600)
    locprocesso = ft.TextField(label="Digite o local o processo se encontra - Cx e instalação", color=cor, width=600)
    
    radio_pesquisa = ft.RadioGroup(content=ft.Row([
                        ft.Radio(value="ano", label="Ano"),
                        ft.Radio(value="UG", label="Unidade Gestora"),
                        ft.Radio(value="numeracao", label="Numeração"),
                        ft.Radio(value="assunto", label="Assunto"),
                        ft.Radio(value="processo", label="Tipo de Processo"),
                        ft.Radio(value="locprocesso", label="localização do Processo"),
                        ]), on_change=criar_pesquisa
                    )
    saida_radio = ft.Text("ano")
    campo_pesquisa = ft.TextField(label="Digite o processo", color=cor, visible=True, on_change=pesquisar)
    
    
    id_atualizar = ft.TextField(label="Digite o Ano do Processo",  color=cor, visible=False)
    ano_atualizar = ft.TextField(label="Digite o Ano do Processo",  color=cor)
    unidadegestoradown_atualizar = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("160039"),
            ft.dropdown.Option("167039"),
        ]
    )
    numeracao_atualizar = ft.TextField(label="Digite o número do Processo", color=cor)
    assunto_atualizar = ft.TextField(label="Digite o assunto do processo", color=cor, width=600)
    tipoprocesso_atualizar = ft.TextField(label="Digite o tipo do processo", color=cor, width=600)
    locprocesso_atualizar = ft.TextField(label="Digite o local o processo se encontra - Cx e instalação", color=cor, width=600)
    dataprotocolo_atualizar = ft.TextField(label="dd/mm/YYYY", keyboard_type = ft.KeyboardType.DATETIME,  color=cor, width=200)
    secaoprotocolo_atualizar = ft.TextField(label="Digite a seção que o doc será protocolado", color=cor, width=390)
    
    categoriaimpressao = ft.Dropdown(
        width=200,
        options=[
            # ft.dropdown.Option(" "),
            ft.dropdown.Option("assunto"),
            ft.dropdown.Option("ano"),
        ]
    )
    
    pesquisa_impressao_relatorio = ft.TextField(label="Digite a pesquisa, para impressão", color=cor, width=600)
    
    imagem = ft.Container(
        image_src="runnergame72.png",
        image_fit=ft.ImageFit.CONTAIN,
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        width=25,
        height=25,
        border_radius=ft.border_radius.all(5),
        )
    
    linha_protocolo = ft.Row(
        [
            dataprotocolo_atualizar,
            secaoprotocolo_atualizar,
        ],
        
    )
    
    linha_conteiner = ft.Container(
        content=ft.Row([
            ft.Column(
                [
                    cabecalho,
                    subtitulo_conteiner,
                    titulo_conteiner,
                ],
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,               
        ),
        
    )
 
    botao_sair = ft.FilledButton(
                    "Sair", 
                    icon=ft.Icons.CLOSE_FULLSCREEN,
                    bgcolor=ft.colors.RED_500,
                    on_click= sair,
                )
    
    botao_cadastrar = ft.FilledButton(
                            "Cadastrar", 
                            icon=ft.Icons.ADD,
                            bgcolor=ft.Colors.BLUE_500,
                            on_click= cadastrar,
                        )
 
    botao_atualizar = ft.FilledButton(
                            "Atualizar", 
                            icon=ft.Icons.UPDATE,
                            bgcolor=ft.colors.BLUE_500,
                            on_click= atualizar,
                        )
    
    botao_apagar = ft.FilledButton(
                    "Apagar", 
                    icon=ft.Icons.DELETE,
                    bgcolor=ft.colors.RED_500,
                    on_click= apagar,
                )

    botao_imprimir = ft.FilledButton(
                    "Imprimir", 
                    icon=ft.Icons.PRINT,
                    bgcolor=ft.colors.AMBER_500,
                    on_click= imprimir,
                )
    
    botao_cancelar = ft.FilledButton(
                    "Cancelar", 
                    icon=ft.Icons.CANCEL_OUTLINED,
                    bgcolor=ft.colors.BLACK26,
                    on_click= cancelar,
                )
 
    botao_imprimir_relatorio = ft.FilledButton(
                            "Imprimir", 
                            icon=ft.Icons.PRINT_ROUNDED,
                            bgcolor=ft.colors.AMBER_500,
                            on_click= impressao_relatório,
                        )
    
    pesquisa = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("id", color=cor, size = 15), visible=False),
                ft.DataColumn(ft.Text("Ano", color=cor, size=15)),
                ft.DataColumn(ft.Text("UG", color=cor, size=15)),
                ft.DataColumn(ft.Text("Numeração", color=cor, size=15)),
                ft.DataColumn(ft.Text("Assunto", color=cor, size=15)),
                ft.DataColumn(ft.Text("Tipo do Processo", color=cor, size=15)),
                ft.DataColumn(ft.Text("Localização", color=cor, size=15)),
                ft.DataColumn(ft.Text("Data Protocolo", color=cor, size=15)),
                ft.DataColumn(ft.Text("Seção Protocolo", color=cor, size=15)),
            ],
            rows=[],
            expand=True,
    )
    
    # dlg_modal = ft.AlertDialog(
    #     modal=True,
    #     title=ft.Text("Impressão Relatório"),
    #     content=categoriaimpressao,
    #     actions=[
    #         ft.TextButton("Sim", on_click=fechardlg),
    #         ft.TextButton("Não", on_click=fechardlg),
    #     ],
    #     actions_alignment=ft.MainAxisAlignment.END,
    #     on_dismiss=lambda e: page.add(
    #         ft.Text("Modal dialog dismissed"),
    #     ),
    # )
    
    atualizar_conteiner = ft.Container(
        visible=False,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        id_atualizar,
                        ano_atualizar,
                        unidadegestoradown_atualizar,
                    ],
                ),
            numeracao_atualizar,
            assunto_atualizar,
            tipoprocesso_atualizar,
            locprocesso_atualizar,
            linha_protocolo,
            ft.Row(controls=[botao_atualizar, botao_apagar, botao_imprimir, botao_cancelar])
            ],
            
        ),
    )
    
    linha_titulo = ft.Row(
                        controls = [
                            titulo_processo,
                        ],
                )
    
       
    linha1 = ft.Row([
        
        # ft.Column(
        #     expand=True,
        #     controls=[
        #         ft.Text(
        #             "Cadastro de Processos",
        #             color=cor,
        #             size=20,
        #             weight="bold",
        #         ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Cadastro de Processos",
                                color=cor,
                                size=20,
                                weight="bold",
                            ),
                            ft.Row(
                                controls=[
                                    
                                    ft.Column(
                                        controls=[
                                            ft.Text(
                                                "Ano:",
                                                color=cor,
                                                size=15,
                                            ),
                                            ano,
                                        ],
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text(
                                                "UG:",
                                                color=cor,
                                                size=15,
                                            ),
                                            unidadegestoradown,
                                        ],
                                    ),
                                ],
                            ),
                            ft.Text(
                                "Numeração:",
                                color=cor,
                                size=15,
                            ),
                            numeracao,
                            
                            ft.Text(
                                "Assunto:",
                                color=cor,
                                size=15,
                            ),
                            assunto,
                
                            ft.Text(
                                    "Tipo:",
                                    color=cor,
                                    size=15,
                                ),
                            tipoprocesso,
                                
                            ft.Text(
                                    "Localização:",
                                    color=cor,
                                    size=15,
                                ),
                            locprocesso,
                            botao_cadastrar,
                        ]
                    ),
                    bgcolor=ft.Colors.BLACK12,
                    width=700,
                    border=ft.border.all(2, ft.Colors.BLACK),
                    padding=ft.padding.all(10),
                    border_radius=10,
                    margin=ft.margin.only(left=50),
                ),

                # ft.Text(
                #     "Numeração:",
                #     color=cor,
                #     size=15,
                # ),
                # numeracao,
                
                # ft.Text(
                #     "Assunto:",
                #     color=cor,
                #     size=15,
                # ),
                # assunto,
                
                # ft.Text(
                #         "Tipo:",
                #         color=cor,
                #         size=15,
                #     ),
                # tipoprocesso,
                    
                # ft.Text(
                #         "Localização:",
                #         color=cor,
                #         size=15,
                #     ),
                # locprocesso,
                # botao_cadastrar,

            ],
        )
    # ],
    # alignment=ft.MainAxisAlignment.CENTER,
    # )
    
    # linha2 = ft.Row(
    #     controls=[

    #         ft.Column(
    #             scroll=ft.ScrollMode.ALWAYS,
    #             controls=[
    #                 ft.Text(
    #                     "Impressão de Relatórios",
    #                     color=cor,
    #                     size=20,
    #                     weight="bold",
    #                 ),
    #                 pesquisa,
    #             ],
    #         ),
    #     ],
    # )

    linha2 = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text(
                    "Impressão de Relatório",
                    color=cor,
                    size=20,
                    weight="bold",
                ),
                ft.Text(
                    "impressão de processo pela categoria:",
                    color=cor,
                    size=15,
                ),
                categoriaimpressao,
                ft.Text(
                    "pesquisa na categoria:",
                    color=cor,
                    size=15,
                ),
                pesquisa_impressao_relatorio,
                botao_imprimir_relatorio,
            ]),
        bgcolor=ft.Colors.BLACK12,
        width=700,
        height=300,
        border=ft.border.all(2, ft.Colors.BLACK),
        padding=ft.padding.all(10),
        border_radius=10,
        margin=ft.margin.only(left=50,),
            
        ),
    ])
    
    linha3 = ft.Row(
        controls=[

            ft.Column(
                controls=[
                    ft.Text(
                        "Relatório",
                        color=cor,
                        size=20,
                        weight="bold",
                    ),
                    atualizar_conteiner,
                    radio_pesquisa,
                    campo_pesquisa,
                    ft.Container(
                        expand=True,
                        content=ft.Row(
                            [ft.Column(
                                controls=[pesquisa],
                                scroll=ft.ScrollMode.ALWAYS #,expand=1,horizontal_alignment=ft.CrossAxisAlignment.START 
                            ),
                        ],
                        scroll=ft.ScrollMode.ALWAYS,expand=1,vertical_alignment=ft.CrossAxisAlignment.START
                        ),
                        width=1090,
                        height=700,
                    ),
                ],
                spacing=5,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    screen_lista= [linha1, linha3, linha2]
    
    principal = ft.Container(
            content=screen_lista[0],
            expand=True,
            alignment=ft.alignment.center      
    )
    
    sidebar_rail_linha=ft.Row(
        controls=[
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                    [  
                        principal,
                    ],
            )
        ],
        expand=True,
    )
    
    
    page.add(
            linha_conteiner,
            linha_titulo,
            sidebar_rail_linha,
            ft.Row(controls=[ft.Container(width=25), botao_sair,ft.Container(expand=True), imagem, ft.Text("by Nelson Luz", color=ft.Colors.BLACK, size=9,), ]),
    )
    


if __name__ == "__main__":
    ft.app(main, assets_dir="assets")