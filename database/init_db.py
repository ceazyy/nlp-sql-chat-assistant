import sqlite3

def create_database():
    conn = sqlite3.connect("database/employees.db")
    cursor = conn.cursor()
    
    # Create Employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Department TEXT NOT NULL,
            Salary NUMERIC NOT NULL,
            Hire_Date DATE NOT NULL
        )
    ''')
    
    # Create Departments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Manager TEXT NOT NULL
        )
    ''')
    
    # Insert sample data into Employees
    cursor.executemany('''
        INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date)
        VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, "Alice", "Sales", 50000, "2021-01-15"),
        (2, "Bob", "Engineering", 70000, "2020-06-10"),
        (3, "Charlie", "Marketing", 60000, "2022-03-20")
    ])
    
    # Insert sample data into Departments
    cursor.executemany('''
        INSERT INTO Departments (ID, Name, Manager)
        VALUES (?, ?, ?)
    ''', [
        (1, "Sales", "Alice"),
        (2, "Engineering", "Bob"),
        (3, "Marketing", "Charlie")
    ])
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    create_database()
