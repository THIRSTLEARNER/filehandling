import sqlite3

# try:
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()
#     print("Database connected successfully!")
# except sqlite3.Error as e:
#   print("Database connection failed:", e)
# finally:
#  if conn:
#   conn.close()

try:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade REAL
    )''')
    conn.commit()
    print("Table created successfully.")
except sqlite3.Error as e:
 print("Error creating table:", e)
finally:
 if conn:
   conn.close() 