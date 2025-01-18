from enum import auto
import flet as ft
from dbdocument import Document


def main(page: ft.Page):
    # page.scroll = "always"
    cor = ft.colors.BLACK54
    page.title = "Sistema de Controle de Documentos"
    # page.bgcolor=ft.colors.WHITE
    
    # page.window_min_width, page.window_max_width = 900, 900
    # page.window_min_height, page.window_max_height = 900, 900
    
    # page.window.width = 200
    # page.window.height = 400
    page.theme_mode=ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary=ft.colors.BLACK54),
    )
    
    
    
    def zeravariaveis():
        ano.value = ""
        unidadegestora.value = ""
        numeracao.value = ""
        assunto.value = ""
        tipoprocesso.value = ""
        locprocesso.value = ""
        page.update()
    
    def zeratualizar():
        id_atualizar.value = ""
        ano_atualizar.value = ""
        unidadegestora_atualizar.value = ""
        numeracao_atualizar.value = ""
        assunto_atualizar.value = ""
        tipoprocesso_atualizar.value = ""
        locprocesso_atualizar.value = ""
        
        atualizar_conteiner.visible = False
        campo_pesquisa.visible = True
        
        campo_pesquisa.update()
        page.update()
    
    def preencher_campos(e):
        atualizar_conteiner.visible=True
        campo_pesquisa.visible=False
        campo_pesquisa.update()
        # print(e.control.cells[0].content.value)
        dooc=Document.get(Document.id==int(e.control.cells[0].content.value))
        id_atualizar.value=dooc.id
        ano_atualizar.value=dooc.ano
        unidadegestora_atualizar.value = dooc.unidadegestora 
        numeracao_atualizar.value = dooc.numeracao
        assunto_atualizar.value = dooc.assunto
        tipoprocesso_atualizar.value = dooc.tipoprocesso
        locprocesso_atualizar.value = dooc.locprocesso
        # print(dooc.ano)
        atualizar_conteiner.update()
    
    def cancelar(e):
        zeratualizar()
        
    def cadastar(e):
        print(f"Cadastro {e}")
        print(f"ano {ano.value}")
        Document.create(ano=ano.value, unidadegestora=unidadegestora.value, numeracao=numeracao.value, assunto=assunto.value,tipoprocesso=tipoprocesso.value, locprocesso=locprocesso.value)
        zeravariaveis()
        
        
    def pesquisar(e):
        
        # query = Facility.select().where(Facility.name.contains('tennis'))
        # print(e.control.value)
        # for assu in Document.select().where(Document.tipoprocesso.contains(e.control.value)):
        preencher_datatable(Document.select().where(Document.tipoprocesso.contains(e.control.value)))
        # for assunto in query:
            # print(f"Pesquisar --> {assu.ano}")
        # querys = (Document.select(Document, fn.CONTAINS(Document.assunto)))
        # for query in querys:
        #     print(f"pesquisar ---> {query.assunto}")
        # print(f"pesquisar---> {pesquisa.rows.DataRow.cells[0]}")
        # for linha in pesquisa.rows:
        #     datacell = linha.cells[0]
        #     linha.visible = (
        #             True
        #         if 
        #             e.control.value.lower() in datacell.content.value.lower() 
        #         else 
        #             False
        #     )
        #     print(f"pesquisar {datacell}")
        #     linha.update()
        # print(f"pesquisa {e}")
    
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
            Document.unidadegestora:unidadegestora_atualizar.value,
            Document.numeracao:numeracao_atualizar.value,
            Document.assunto:assunto_atualizar.value,
            Document.tipoprocesso:tipoprocesso_atualizar.value,
            Document.locprocesso:locprocesso_atualizar.value,
            }).where(Document.id==id_atualizar.value)
        print(f"funcao atualizar: {atualizacao}")
        
        atualizacao.execute()
        
        zeratualizar()
        campo_pesquisa.value=""
        preencher_datatable(Document.select())
        pesquisa.update()
    
    def preencher_datatable(query):
        print(f"teste {query}")
        cores=[ft.colors.GREEN_50, ft.colors.BLACK45]
        pesquisa.rows.clear()
        for i, doc in enumerate(query, 1):
            # print(f"DocumentoXXXXXX: {doc.id, doc.ano, doc.unidadegestora, doc.numeracao, doc.assunto, doc.tipoprocesso, doc.locprocesso}")
            pesquisa.rows.append(
                
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(doc.id), visible=False), 
                    ft.DataCell(ft.Text(doc.ano, color=cor, size=15,  on_tap=preencher_campos,)), 
                    ft.DataCell(ft.Text(doc.unidadegestora, color=cor, size=15)), 
                    ft.DataCell(ft.Text(doc.numeracao, color=cor, size=15)),
                    ft.DataCell(ft.Text(doc.assunto, color=cor, size=15)),  
                    ft.DataCell(ft.Text(doc.tipoprocesso, color=cor, size=15)), 
                    ft.DataCell(ft.Text(doc.locprocesso, color=cor, size=15)),
                    ],
                    color=cores[i%2],
                    on_select_changed=preencher_campos,
                    # on_long_press=preencher_campos,
                    )
            )
            # pesquisa.rows.append(linhas)
        page.update()
    
    def set_screen(e):
        print(e)
        # cores=["#759DCB", "#DABD90"]
        # cores=[ft.colors.GREEN_50, ft.colors.BLACK45]
        principal.content=screen_lista[e.control.selected_index]
        if e.control.selected_index == 1:
            preencher_datatable(Document.select())
        #     pesquisa.rows.clear()
        #     for i, doc in enumerate(Document.select(), 1):
        #         print(f"Documento: {doc.id, doc.ano, doc.unidadegestora, doc.numeracao, doc.assunto, doc.tipoprocesso, doc.locprocesso}")
        #         pesquisa.rows.append(
                    
        #             ft.DataRow(cells=[
        #                 ft.DataCell(ft.Text(doc.id), visible=False), 
        #                 ft.DataCell(ft.Text(doc.ano, color=cor, size=15,  on_tap=preencher_campos,)), 
        #                 ft.DataCell(ft.Text(doc.unidadegestora, color=cor, size=15)), 
        #                 ft.DataCell(ft.Text(doc.numeracao, color=cor, size=15)),
        #                 ft.DataCell(ft.Text(doc.assunto, color=cor, size=15)),  
        #                 ft.DataCell(ft.Text(doc.tipoprocesso, color=cor, size=15)), 
        #                 ft.DataCell(ft.Text(doc.locprocesso, color=cor, size=15)),
        #                 ],
        #                 color=cores[i%2],
        #                 on_select_changed=preencher_campos,
        #                 # on_long_press=preencher_campos,
        #                 )
        #         )
        #         # pesquisa.rows.append(linhas)
        page.update()
    
    rail = ft.NavigationRail(
        # expand=True,
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
            # ft.NavigationRailDestination(
            #     icon=ft.Icons.SEARCH_OUTLINED,
            #     selected_icon=ft.Icons.SEARCH,
            #     label="Pesquisa",
                
            # ),
        ],
        on_change=set_screen,  
    )
    
    titulo = "Sistema de Controle de Documentos"
    subtitulo = "Conformidade"
    titulo_conteiner = ft.Container(
        content = ft.Text(titulo,
                    size=20,
                    color=cor,
                    weight="bold",
                ),
        bgcolor = ft.Colors.BLUE_900,
        border_radius = ft.border_radius.all(25),
        padding = 15,
        # alignment=ft.MainAxisAlignment.CENTER,
    )
    subtitulo_conteiner = ft.Container(
        content = ft.Text(subtitulo,
                    size=20,
                    color=cor,
                    weight="bold",
        ),
        # alignment=ft.Alignment.CENTER,
        margin=ft.margin.only(left=120),
        # width=150,
        # height=150,
        padding= 15,
        bgcolor = ft.Colors.BLUE_900,
        border_radius = ft.border_radius.all(25),
        # padding = 5
    )
    titulo_processo = ft.Text(
        "Contole de Processos arquivado na Conformidade",
        color=cor,
        size=25,
        weight="bold",
    )
    
    ano = ft.TextField(label="Digite o Ano do Processo",  color=cor)
    unidadegestora = ft.TextField(label="Digite a Unidade Gestora", color=cor, max_length=6)
    numeracao = ft.TextField(label="Digite o número do Processo", color=cor)
    assunto = ft.TextField(label="Digite o tipo do processo", color=cor, width=600)
    tipoprocesso = ft.TextField(label="Digite o tipo do processo", color=cor, width=600)
    locprocesso = ft.TextField(label="Digite o local o processo se encontra - Cx e instalação", color=cor, width=600)
    
    campo_pesquisa = ft.TextField(label="Digite o processo", color=cor, visible=True, on_change=pesquisar)
    
    id_atualizar = ft.TextField(label="Digite o Ano do Processo",  color=cor, visible=False)
    ano_atualizar = ft.TextField(label="Digite o Ano do Processo",  color=cor)
    unidadegestora_atualizar = ft.TextField(label="Digite a Unidade Gestora", color=cor, max_length=6)
    numeracao_atualizar = ft.TextField(label="Digite o número do Processo", color=cor)
    assunto_atualizar = ft.TextField(label="Digite o tipo do processo", color=cor, width=600)
    tipoprocesso_atualizar = ft.TextField(label="Digite o tipo do processo", color=cor, width=600)
    locprocesso_atualizar = ft.TextField(label="Digite o local o processo se encontra - Cx e instalação", color=cor, width=600)
    
    
    linha_conteiner = ft.Container(
        # expand=True,
        content=ft.Row([
            ft.Column(
                [
                    titulo_conteiner,
                    subtitulo_conteiner,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        # margin=ft.margin.only(left=300),
        ],
        alignment=ft.MainAxisAlignment.CENTER,               
        ),
    )
 
    botao_cadastrar = ft.FilledButton(
                            "Cadastrar", 
                            icon=ft.Icons.ADD,
                            bgcolor=ft.Colors.BLUE_100,
                            # size=20,
                            # padding=15,
                            on_click= cadastar,
                        )
 
    botao_atualizar = ft.FilledButton(
                            "Atualizar", 
                            icon=ft.Icons.UPDATE,
                            bgcolor=ft.colors.BLUE_100,
                            # size=20,
                            # padding=15,
                            on_click= atualizar,
                        )
    
    botao_apagar = ft.FilledButton(
                    "Apagar", 
                    icon=ft.Icons.DELETE,
                    bgcolor=ft.colors.BLUE_100,
                    # size=20,
                    # padding=15,
                    on_click= apagar,
                )
    
    botao_cancelar = ft.FilledButton(
                    "Cancelar", 
                    icon=ft.Icons.CANCEL_OUTLINED,
                    bgcolor=ft.colors.BLUE_100,
                    # size=20,
                    # padding=15,
                    on_click= cancelar,
                )
    
    pesquisa = ft.DataTable(
        # expand=True,
            # scroll="always",
            columns=[
                ft.DataColumn(ft.Text("id", color=cor, size = 15), visible=False),
                ft.DataColumn(ft.Text("Ano", color=cor, size=15)),
                ft.DataColumn(ft.Text("UG", color=cor, size=15)),
                ft.DataColumn(ft.Text("Numeração", color=cor, size=15)),
                ft.DataColumn(ft.Text("TAssunto", color=cor, size=15)),
                ft.DataColumn(ft.Text("Tipo do Processo", color=cor, size=15)),
                ft.DataColumn(ft.Text("Localização", color=cor, size=15)),
            ],
            rows=[],
            expand=True,
    )
    
    atualizar_conteiner = ft.Container(
        expand=True,
        visible=False,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        id_atualizar,
                        ano_atualizar,
                        unidadegestora_atualizar,
                    ],
                ),
            numeracao_atualizar,
            assunto_atualizar,
            tipoprocesso_atualizar,
            locprocesso_atualizar,
                ft.Row(controls=[botao_atualizar, botao_apagar, botao_cancelar])
            ],
        ),
    )
    
    linha_titulo = ft.Row(
                    controls = [
                        titulo_processo,
                    ],
                )
    

        
    linha1 = ft.Row([
        
        ft.Column(
            expand=True,
            controls=[
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
                                unidadegestora,
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
                
                # ft.Row(
                #     controls=[
                #         botao_cadastrar,
                #     ],
                # ),
            ],
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    )
    
    linha2 = ft.Row(
        # expand=True,
        controls=[

            ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                # on_scroll=on_column_scroll,
                controls=[
                    ft.Text(
                        "Relatório",
                        color=cor,
                        size=20,
                        weight="bold",
                    ),
                    pesquisa,
                ],
            ),
        ],
    )

    linha3 = ft.Row(
        controls=[

            ft.Column(
                scroll="always",
                controls=[
                    ft.Text(
                        "Relatório",
                        color=cor,
                        size=20,
                        weight="bold",
                    ),
                    atualizar_conteiner,
                    campo_pesquisa,
                    # botao_pesquisar,
                    pesquisa,
                ],
                spacing=5,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    screen_lista= [linha1, linha3, linha2]
    
    principal = ft.Container(
            content=screen_lista[0],
            # expand=True,        
    )
    
    sidebar_rail_linha=ft.Row(
        # expand=True,
        controls=[
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                [  
                    # principal, 
                    principal,
                    # botao_cadastrar,
                ],
            ),
        ],
        expand=True,
    )
    
    
    page.add(
            linha_conteiner,
            linha_titulo,
            sidebar_rail_linha,
            # ft.Container(
            #     content=ft.ElevatedButton("Page theme button"),
            #     bgcolor=ft.Colors.ON_SURFACE_VARIANT,
            #     padding=20,
            #     width=300,
            # ),
    )
    
    




if __name__ == "__main__":
    ft.app(main)