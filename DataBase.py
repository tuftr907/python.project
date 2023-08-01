import sqlite3
conn = sqlite3.connect('patient_records.db') 
cursor = conn.cursor()
cursor.execute('SELECT * FROM patients')
rows = cursor.fetchall()
for row in rows:
    print("Name: {}, Age: {}, Height: {}, Oxygen Level: {}, Heart Rate: {}, Blood Group: {}, Blood Pressure: {}".format(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
cursor.close()
conn.close()
