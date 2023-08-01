import sqlite3
conn = sqlite3.connect('file_name.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS patients
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              age INTEGER,
              height REAL,
              oxygen_level REAL,
              heart_rate INTEGER,
              blood_group TEXT,
              blood_pressure TEXT)''')
class PatientRecord:
    def __init__(self, name, age, height, oxygen_level, heart_rate, blood_group, blood_pressure):
        self.name = name
        self.age = age
        self.height = height
        self.oxygen_level = oxygen_level
        self.heart_rate = heart_rate
        self.blood_group = blood_group
        self.blood_pressure = blood_pressure
        
    def update_record(self, field, value):
        if field == 'name':
            self.name = value
        elif field == 'age':
            self.age = value
        elif field == 'height':
            self.height = value
        elif field == 'oxygen_level':
            self.oxygen_level = value
        elif field == 'heart_rate':
            self.heart_rate = value
        elif field == 'blood_group':
            self.blood_group = value
        elif field == 'blood_pressure':
            self.blood_pressure = value
        else:
            print("invalid field")
    
        c.execute("UPDATE patients SET {} = ? WHERE name = ?".format(field), (value, self.name))
        conn.commit()

    def delete_record(self):
        c.execute("DELETE FROM patients WHERE name = ?", (self.name,))
        conn.commit()
        del self.name
        del self.age
        del self.height
        del self.oxygen_level
        del self.heart_rate
        del self.blood_group
        del self.blood_pressure
        print("Patient record deleted")

    def take_user_input( ):
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        height = float(input("Enter patient height (in cm): "))
        oxygen_level = float(input("Enter patient oxygen level: "))
        heart_rate = int(input("Enter patient heart rate: "))
        blood_group = input("Enter patient blood group: ")
        blood_pressure = input("Enter patient blood pressure: ")
        return name, age, height, oxygen_level, heart_rate, blood_group, blood_pressure


    
num_patients = int(input("Enter the number of patients: "))
patients = []

for i in range(num_patients):
    print(f"Enter details for Patient {i + 1}:")
    name, age, height, oxygen_level, heart_rate, blood_group, blood_pressure = PatientRecord.take_user_input()
    patient = PatientRecord(name, age, height, oxygen_level, heart_rate, blood_group, blood_pressure)
    patients.append(patient)
    c.execute("INSERT INTO patients (name, age, height, oxygen_level, heart_rate, blood_group, blood_pressure) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, age, height, oxygen_level, heart_rate, blood_group, blood_pressure))
    conn.commit()
choice = input("Enter 'u' to update or 'd' to delete: ")
if choice == 'u':
    patient_idx = int(input("Enter the patient index to update (0 to {}): ".format(num_patients - 1)))
    if patient_idx >= 0 and patient_idx < num_patients:
       field = input("Enter field to update: ")
       value = input("Enter new value: ")
       patients[patient_idx].update_record(field, value)
    else:
        print("Invalid patient index.")
elif choice == 'd':
    patient_idx = int(input("Enter the patient index to delete (0 to {}): ".format(num_patients - 1)))
    if patient_idx >= 0 and patient_idx < num_patients:
        confirm = input("Are you sure you want to delete this patient's record? (yes/no): ")
        if confirm.lower() == 'yes':
            patients[patient_idx].delete_record()
            del patients[patient_idx]
            print("Patient record deleted")
        elif confirm.lower() == 'no':
            print("Deletion cancelled.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid patient index.")
else:
    print("Invalid choice.")
print("____________________________________________________________________________________")   
print("Updated information of all patients:")
for i, patient in enumerate(patients):
    print(f"Patient {i + 1}:")
    print(f"Name: {patient.name}, Age: {patient.age}, Height: {patient.height}, Oxygen Level: {patient.oxygen_level}, Heart Rate: {patient.heart_rate}, Blood Group: {patient.blood_group}, Blood Pressure: {patient.blood_pressure}")
print("____________________________________________________________________________________")
conn.commit()
conn.close()
