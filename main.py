from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):
  title = "Moje kalkulačka"

  def build(self):
    self.main_layout = GridLayout(cols = 1, padding = 10, spacing = 10)
    self.display = TextInput(
      multiline = False,
      readonly = True,
      halign = "right",
      font_size = 55
    )
    self.main_layout.add_widget(self.display)

    buttons_layout = GridLayout(cols = 4, spacing = 10)

    buttons = [
      "7", "8", "9", "/",
      "4", "5", "6", "*",
      "1", "2", "3", "-",
      ".", "0", "=", "+",
      "C", "<-",
    ]

    for button_text in buttons:
      button = Button(text = button_text)
      button.bind(on_press = self.on_button_press)
      buttons_layout.add_widget(button)

    self.main_layout.add_widget(buttons_layout)

    return self.main_layout

  def on_button_press(self, instance):
    current_text = self.display.text
    button_text = instance.text

    if button_text == "=":
      try:
        self.display.text = str(eval(current_text))
      except Exception:
        self.display.text = "Error"
    elif button_text == "C":
      self.display.text = ""
    elif button_text == "<-":
      self.display.text = current_text[:-1]
    else:
      self.display.text += button_text

MainApp().run()