import sqlite3
import re

def connect_db():
    return sqlite3.connect("database/employees.db")

def process_query(user_input):
    """Convert natural language queries into SQL and execute them."""
    conn = connect_db()
    cursor = conn.cursor()
    
    # Define query patterns
    patterns = {
        "employees_in_department": r"show me all employees in the (.+) department",
        "manager_of_department": r"who is the manager of the (.+) department\?",
        "employees_hired_after": r"list all employees hired after (\d{4}-\d{2}-\d{2})",
        "total_salary_expense": r"what is the total salary expense for the (.+) department\?",
        "employee_contact": r"what is the contact information of (.+)",
        "employee_experience": r"how much experience does (.+) have\?",
        "department_budget": r"what is the budget for the (.+) department\?",
        "department_location": r"where is the (.+) department located\?",
        "employees_by_position": r"list all (.+) in the company",
        "highest_paid_employee": r"who is the highest paid employee\?",
        "average_salary_department": r"what is the average salary in the (.+) department\?",
        "employees_with_experience": r"list all employees with more than (\d+) years of experience",
        "employees_by_hire_year": r"who were hired in the year (\d{4})\?",
        "specific_employee_details": r"give me details of (.+)",
        "employees_by_email_domain": r"list all employees with email domain (.+)"
    }
    
    match = None
    sql_query = None
    params = ()
    
    if re.match(patterns["employees_in_department"], user_input, re.IGNORECASE):
        match = re.search(patterns["employees_in_department"], user_input, re.IGNORECASE)
        department = match.group(1).strip()
        sql_query = "SELECT Name, Salary, Hire_Date FROM Employees WHERE Department = ?"
        params = (department,)
    
    elif re.match(patterns["manager_of_department"], user_input, re.IGNORECASE):
        match = re.search(patterns["manager_of_department"], user_input, re.IGNORECASE)
        department = match.group(1).strip()
        sql_query = "SELECT Manager FROM Departments WHERE Name = ?"
        params = (department,)
    
    elif re.match(patterns["employees_hired_after"], user_input, re.IGNORECASE):
        match = re.search(patterns["employees_hired_after"], user_input, re.IGNORECASE)
        hire_date = match.group(1).strip()
        sql_query = "SELECT Name, Department, Hire_Date FROM Employees WHERE Hire_Date > ?"
        params = (hire_date,)
    
    elif re.match(patterns["total_salary_expense"], user_input, re.IGNORECASE):
        match = re.search(patterns["total_salary_expense"], user_input, re.IGNORECASE)
        department = match.group(1).strip()
        sql_query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
        params = (department,)
    
    elif re.match(patterns["employee_contact"], user_input, re.IGNORECASE):
        match = re.search(patterns["employee_contact"], user_input, re.IGNORECASE)
        name = match.group(1).strip()
        sql_query = "SELECT Email, Phone FROM Employees WHERE Name = ?"
        params = (name,)
    
    elif re.match(patterns["employee_experience"], user_input, re.IGNORECASE):
        match = re.search(patterns["employee_experience"], user_input, re.IGNORECASE)
        name = match.group(1).strip()
        sql_query = "SELECT Experience FROM Employees WHERE Name = ?"
        params = (name,)
    
    elif re.match(patterns["department_budget"], user_input, re.IGNORECASE):
        match = re.search(patterns["department_budget"], user_input, re.IGNORECASE)
        department = match.group(1).strip()
        sql_query = "SELECT Budget FROM Departments WHERE Name = ?"
        params = (department,)
    
    elif re.match(patterns["department_location"], user_input, re.IGNORECASE):
        match = re.search(patterns["department_location"], user_input, re.IGNORECASE)
        department = match.group(1).strip()
        sql_query = "SELECT Location FROM Departments WHERE Name = ?"
        params = (department,)
    
    if sql_query:
        cursor.execute(sql_query, params)
        result = cursor.fetchall()
        conn.close()
        return result if result else "No results found."
    
    conn.close()
    return "Sorry, I didn't understand your query. Please try again."

if __name__ == "__main__":
    while True:
        user_input = input("Ask a question: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = process_query(user_input)
        print(response)
