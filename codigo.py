import flet as ft


def main(pagina):
    texto = ft.Text("HashZap")
    botao_iniciar = ft.ElevatedButton("iniciar chat")
    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER)

