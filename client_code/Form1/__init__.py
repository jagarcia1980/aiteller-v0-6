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
    self.button_1.enabled=False #paso 1
    self.button_3.enabled=True #paso 2
    self.button_2.text="MODIFICAR VALORES"
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
    self.button_3.enabled=False # paso 2
    self.button_5.enabled=True # paso 3
    self.button_4.text="VOLVER A GENERAR"
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.txtcodigo.visible=False
    self.label_2.visible=False
    self.txtlugar.visible=False
    self.label_3.visible=False
    self.txttematica.visible=False
    self.label_4.visible=False
    self.txtprotagonista.visible=False
    self.button_2.visible=False
    self.button_4.visible=False
    self.rich_text_1.visible=False
    self.rich_text_2.visible=True
    self.rich_text_2.content=anvil.server.call('callable_paso1_4')
    self.button_6.visible=True
    self.button_5.enabled=False
    self.button_7.enabled=True
    pass

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_5_click()
    pass

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible=False
    self.txtcodigo.visible=False
    self.label_2.visible=False
    self.txtlugar.visible=False
    self.label_3.visible=False
    self.txttematica.visible=False
    self.label_4.visible=False
    self.txtprotagonista.visible=False
    self.button_2.visible=False
    self.button_4.visible=False
    self.button_6.visible=False
    self.rich_text_1.visible=False
    self.rich_text_2.visible=False
    self.rich_text_3.visible=True
    self.rich_text_3.content=anvil.server.call('callable_paso1_5')
    self.rich_text_3.content=self.rich_text_3.content+"<br/><br/>" + anvil.server.call('callable_paso1_6', "")
    self.rich_text_3.content=self.rich_text_3.content+"<br/><br/>" + anvil.server.call('callable_paso1_7', "")
    pass
    
