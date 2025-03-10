import sqlite3

connection = sqlite3.connect("hr.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Employees
                (Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Position TEXT, Salary INTEGER, Dep_ID INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Departments
                (Dep_ID INTEGER, Department_Name TEXT)''')

employees = [("John Clever", "Software Engineer", 1000, 111),
             ("Edy Lucky", "Technical Team Lead", 2000, 111),
             ("Peter Park", "Sales Specialist", 1000, 222)]

departments = [("111", "IT"), ("222", "Sales")]

#cursor.executemany('''INSERT INTO Employees (Name,Position,Salary,Dep_ID) VALUES (?,?,?,?)''', employees)
#cursor.executemany(''' INSERT INTO Departments (Dep_ID, Department_Name) VALUES (?,?)''', departments)
result = cursor.execute('''SELECT * FROM Employees join Departments ON Employees.Dep_ID = Departments.Dep_ID''')

print(result.fetchall())
connection.commit()
connection.close()
