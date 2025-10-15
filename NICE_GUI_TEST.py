from nicegui import ui

@ui.page('/')
def main_page():
    name = ui.input('Your name')
    ui.button('Say Hello', on_click=lambda: ui.notify(f'Hello {name.value}!'))

ui.run()
