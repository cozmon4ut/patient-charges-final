# Cosmo H, CIS129 Final
# Dec 2023


"""This class handles any data regarding the patient"""
class Patient: 
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip, phone_number, emergency_name, emergency_phone_number):
        # Needed data fields
        self.first_name = first_name 
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.emergency_name = emergency_name
        self.emergency_phone_number = emergency_phone_number
        
    # Accessor methods
    def getFirstName(self):
        return self.first_name
    
    def getMiddleName(self):
        return self.middle_name
    
    def getLastName(self):
        return self.last_name
    
    def getAddress(self):
        return self.address
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getZip(self):
        return self.zip
    
    def getPhoneNumber(self):
        return self.phone_number
    
    def getEmergencyName(self):
        return self.emergency_name
    
    def getEmergencyNumber(self):
        return self.emergency_phone_number 

    # Mutator methods
    def setFirstName(self, first_name):
        self.first_name = first_name
    
    def setMiddleName(self, middle_name):
        self.middle_name = middle_name
    
    def setLastName(self, last_name):
        self.last_name = last_name
    
    def setAddress(self, address):
        self.address = address
    
    def setCity(self, city):
        self.city = city
    
    def setState(self, state):
        self.state = state
    
    def setZip(self, zip):
        self.zip = zip
    
    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number
    
    def setEmergencyName(self, emergency_name):
        self.emergency_name = emergency_name
    
    def setEmergencyNumber(self, emergency_phone_number):
        self.emergency_phone_number = emergency_phone_number

"""This class is for data pertaining the procedure being performed"""

class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner_name, procedure_charges):
        # Necessary data fields  
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practitioner_name = practitioner_name
        self.procedure_charges = procedure_charges
    
    # Accessor methods
    def getProcedureName(self):
        return self.procedure_name
    
    def getProcedureDate(self):
        return self.procedure_date    
    
    def getPractitionerName(self):
        return self.practitioner_name
    
    def getProcedureCharges(self):
        return self.procedure_charges
    
    # Mutator methods 
    def setProcedureName(self, procedure_name):
        self.procedure_name = procedure_name
    
    def setProcedureDate(self, procedure_date):
        self.procedure_date = procedure_date
    
    def setPractitonerName(self, practitioner_name):
        self.practitioner_name = practitioner_name
    
    def setProcedureCharges(self, procedure_charges):
        self.procedure_charges = procedure_charges

    
 