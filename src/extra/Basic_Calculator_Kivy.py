#
import math
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
Window.size = (400, 600)


class BasicCalculator(App):

    def build(self):
        blue = '204b99'

        self.title = 'Kivy: Basic Calculator'
        root_widget = BoxLayout(orientation='vertical')
        output_label = Label(size_hint_y=0.75, font_size=50)
        button_grid = GridLayout(cols=4, size_hint_y=2)
        buttons = {
            '0': {'text': '1/x', 'type': 'number'},
            '1': {'text': 'x*x', 'type': 'number'},
            '2': {'text': 'sqrt(x)', 'type': 'number'},
            '3': {'text': '/', 'type': 'op'},

            '4': {'text': '7', 'type': 'number'},
            '5': {'text': '8', 'type': 'number'},
            '6': {'text': '9', 'type': 'number'},
            '7': {'text': 'x', 'type': 'op'},

            '8': {'text': '4', 'type': 'number'},
            '9': {'text': '5', 'type': 'number'},
            '10': {'text': '6', 'type': 'number'},
            '11': {'text': '-', 'type': 'op'},

            '12': {'text': '1', 'type': 'number'},
            '13': {'text': '2', 'type': 'number'},
            '14': {'text': '3', 'type': 'number'},
            '15': {'text': '+', 'type': 'op'},

            '16': {'text': '+/-', 'type': 'number'},
            '17': {'text': '0', 'type': 'number'},
            '18': {'text': '.', 'type': 'number'},
            '19': {'text': '=', 'type': 'op'},
        }
        for key in buttons:
            button_grid.add_widget(Button(text=buttons[key]['text'], font_size=20, background_color=blue))

        def print_button_text(instance):
            if instance.text == 'x':
                output_label.text += '*'
            elif instance.text == '1/x':
                output_label.text = str(1/int(output_label.text))
            elif instance.text == 'x*x':
                output_label.text = str(int(output_label.text)**2)
            elif instance.text == 'sqrt(x)':
                output_label.text = str(math.sqrt(int(output_label.text)))
            elif instance.text == '+/-':
                if output_label.text != '' and int(output_label.text) > 0:
                    output_label.text = "-"+str(int(output_label.text))
                elif output_label.text == '':
                    output_label.text = "-"
                else:
                    output_label.text = str(math.fabs(int(output_label.text)))
            else:
                output_label.text += instance.text
        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)

        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Python Syntax error!'

        button_grid.children[0].bind(on_press=evaluate_result)

        def clear_label(instance):
            output_label.text = " "

        clear_button = Button(text='Clear', size_hint_y=None, height=60)
        clear_button.bind(on_press=clear_label)

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)
        return root_widget


BasicCalculator().run()