import sqlite3
from db import cursor
from helper_db import select_data, insert_execution, insert_multiple_execution


conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    age INTEGER
    )
    ''')
    
    
students = [
    {"name": "Sophia f", "gender": "female", "age": 15},
    {"name": "Semen", "gender": "male", "age": 13},
    {"name": "Illya", "gender": "male", "age": 15},
    {"name": "Vlad", "gender": "male", "age": 16},
    {"name": "Vova", "gender": "male", "age": 15},
    {"name": "Rostyslav", "gender": "male", "age": 14},
]


for student in students:
    cursor.execute('''
    INSERT INTO students (name, gender, age)
    VALUES (?, ?, ?)
    ''', (student['name'], student['gender'], student['age']))

conn.commit()

def display_students():
    cursor.execute('''
    SELECT * FROM students
    ''')
    students = cursor.fetchall()
    
    for student in students:
        print(f"Name: {student[1]}, Gender: {student[2]}, Age: {student[3]}")

display_students()
# developers_insert_execution("Sofiia", "sofiia.fedorenko@gmail.com", "2024-12-15", 200.5)
# developers_insert_execution("Vlad", "vlad.khmara@gmail.com", "2024-12-15", 200.5)

# records = [
#     ("Vova", "vova.stepanenko@gmail.com", "2024-12-15", 200.5),
#     ("Semen", "semen.savenkov@gmail.com", "2024-12-15", 200.5),
# ]

# insert_multiple_execution(records)

records = select_data("developers", 3)

print(records)

# for record in records:
#     print(record[1])

cursor.close()
