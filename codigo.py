import flet as ft


def main(pagina):
    texto = ft.Text("HashZap")

    nome_usuario = ft.TextField(label='Escreva seu nome')

    campo_mensagem = ft.TextField(label='Escreva sua mensagem')
    botao_enviar_mensagem = ft.ElevatedButton('Enviar Mansagem')

    chat =ft.Column()
    def entrar_popup(e):
        pagina.add(chat)
        popup.open = False
        pagina.remove(texto)
        pagina.remove(botao_iniciar)
        pagina.add(ft.Row([campo_mensagem,botao_enviar_mensagem]))

        pagina.update()


    popup = ft.AlertDialog(open=False, modal=True, title=ft.Text("Bem vindo ao HashZap"),
                           content=nome_usuario, actions=[ft.ElevatedButton('Entrar',on_click=entrar_popup)],)

    def entrar_chat(e):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("iniciar chat", on_click=entrar_chat)
    pagina.add(texto)
    pagina.add(botao_iniciar)








ft.app(target=main, view=ft.WEB_BROWSER)

