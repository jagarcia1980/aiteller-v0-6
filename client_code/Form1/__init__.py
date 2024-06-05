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
    self.label_1.visible=True
    self.txtcodigo.visible=True
    self.label_2.visible=True
    self.txtlugar.visible=True
    self.label_3.visible=True
    self.txttematica.visible=True
    self.label_4.visible=False
    self.txtprotagonista.visible=False
    self.button_2.visible=True
    self.button_4.visible=False
    
    self.rich_text_1.content=""
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.rich_text_1.content=anvil.server.call('callable_paso1_2', 
      self.txtcodigo.text,self.txtlugar.text,self.txttematica.text)

    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.txtcodigo.visible=False
    self.label_2.visible=False
    self.txtlugar.visible=False
    self.label_3.visible=False
    self.txttematica.visible=False
    self.label_4.visible=True
    self.txtprotagonista.visible=True
    self.button_2.visible=False
    self.button_4.visible=True
    self.rich_text_1.content=""
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_1.content=anvil.server.call('callable_paso1_3', 
      self.txtprotagonista.text)
    self.button_4.text="VOLVER A GENERAR"
    pass
    
