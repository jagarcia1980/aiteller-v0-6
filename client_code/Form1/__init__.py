from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.rich_text_1.content="<b>negrita</b><h3>encabezado</h3>"
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.rich_text_1.content=anvil.server.call('callable_paso1_2', 
      self.txtcodigo.text,self.txtlugar.text,self.txttematica.text)

    pass
    
