from ._anvil_designer import signupTemplate
from anvil import *
import anvil.server

class signup(signupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("dashboard")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("login")