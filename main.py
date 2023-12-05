# Cosmo H, CIS129 Final
# Dec 2023
from patient_charges import Patient, Procedure
from datetime import datetime

# Variable to store the current date when the program is run
todays_date = datetime.today().strftime("%m-%d-%Y")
# Patient object with dummy data
patient = Patient("Cosmo", "Lee", "Herzig", "1234 Street Blvd", "Dover", "Delaware", "010101", "1-867-5309", "Lukas H, 1-234-5678")
# Procedure objects
procedure_1 = Procedure("Physical Exam", todays_date, "Dr. Irvine", "$250.00")
procedure_2 = Procedure("X-ray", todays_date, "Dr. Jamison", "$500.00")
procedure_3 = Procedure("Blood test", todays_date, "Dr. Smith", "$200.00")

def main():
    print("_" * 50)
    print(f"Patient information: \n{patient.getFirstName()} {patient.getMiddleName()} {patient.getLastName()} \nPhone Number: {patient.getPhoneNumber()}")
    print(f"Address: {patient.getAddress()}, {patient.getCity()}, {patient.getState()} {patient.getZip()}")
    print(f"Emergency Contact: {patient.getEmergencyName()}, {patient.getEmergencyNumber()}")

    # Initiate a for loop for the purpose of using only one print statement for each procedure instance
    procedure_range = range(1, 4)
    for i in procedure_range:
        procedure_instance = globals()[f"procedure_{i}"] # Get the procedure instance dynamically so the range can be used correctly
        print("_" * 50)
        print(f"""Procedure {i}: {getattr(procedure_instance, 'getProcedureName')()}\nDate: {getattr(procedure_instance, 'getProcedureDate')()}
    Practitioner: {getattr(procedure_instance, 'getPractitionerName')()}\nCharge {getattr(procedure_instance, 'getProcedureCharges')()}""")

    print("_" * 50)

if __name__ == "__main__":
    main()