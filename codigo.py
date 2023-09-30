import flet as ft


def main(pagina):
    texto = ft.Text("HashZap")

    nome_usuario = ft.TextField(label='Escreva seu nome')

    campo_mensagem = ft.TextField(label='Escreva sua mensagem')

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat",
                                 size=12, italic=True, color =ft.colors.BLUE_500))



        campo_mensagem.value = ""
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(e):

        pagina.pubsub.send_all({"texto": campo_mensagem.value,
                                "usuario": nome_usuario.value,
                                "tipo": "mensagem"})

        campo_mensagem.value = ""

        pagina.update()

    botao_enviar_mensagem = ft.ElevatedButton('Enviar Mansagem', on_click=enviar_mensagem)


    def entrar_popup(e):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
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


ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

