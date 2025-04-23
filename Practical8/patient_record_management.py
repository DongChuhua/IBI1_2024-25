#Create a class	called ‘patients’ 
#which contains the following attributes: patient name; age; date of latest admission; and medical history
class patients:
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history

    def details(self):
        return f"Patient Name: {self.name}, Age: {self.age}, Admission Date: {self.admission_date}, Medical History: {self.medical_history}"

# example usage:   
patient_x = patients("DongChuhua", 18, "2025-04-08", "fever")
print(patient_x.details())