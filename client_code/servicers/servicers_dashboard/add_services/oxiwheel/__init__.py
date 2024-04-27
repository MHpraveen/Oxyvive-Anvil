from ._anvil_designer import oxiwheelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string


class oxiwheel(oxiwheelTemplate):
  def __init__(self, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = user_id
    self.first_file_name = None
    self.second_file_name = None
    self.file1 = None
    self.file2 = None


 
  def next_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    vehicle_no  = self.hospital_name.text
    model_year = self.oxiclini_established_year.date
    state = self.state.text
    district = self.district.text
    pincode = self.oxiclinic_pincode.text
    address = self.oxiclinic_address.text
    capsule = self.oxiclinic_capsules.text

    if (
      not vehicle_no
      and not address
      and not capsule
      and not district
      and not model_year
      and not pincode
      and not state
      and not self.first_file_name
      and not self.second_file_name
    ):
      Notification('All "Fields" and "Documents"  are required.').show()
    else:
      user_details = app_tables.users.get(id=self.user_id)
      print(user_details)
      app_tables.oxiwheels.add_row(
        id=str(user_details["id"]),
        name=user_details["username"],
        email=user_details["email"],
        password=user_details["password"],
        phone=int(user_details["phone"]),
        pincode=int(pincode),
        Oxiwheels_Name=vehicle_no,
        model_year=str(model_year),
        State=state,
        District=district,
        address_2=address,
        capsules=int(capsule),
        vehicle_rc=self.file1,
        driving_licence=self.file2,
        oxywheel_id=self.generate_unique_random_code()
      )

      alert("You added oxiwheel successfully.")

      open_form("servicers.servicers_dashboard.add_services", id=self.user_id)

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.first_file_name = file.get_name()
    self.file_name_1.text = self.first_file_name
    self.file1 = file
    self.file_loader_1.text = "Selected"

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.second_file_name = file.get_name()
    self.file_name_2.text = self.second_file_name
    self.file2 = file
    self.file_loader_2.text = "Selected"

  def generate_unique_random_code(self):
    prefix = "OW"
    while True:
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        code = prefix + random_numbers
        
        # Check if the code already exists in the data table
        existing_rows = app_tables.oxiwheels.get(oxywheel_id=code)
        if not existing_rows:
            # If the code does not exist, return it
            return code
