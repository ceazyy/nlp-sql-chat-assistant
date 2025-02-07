import sqlite3
import re
import gradio as gr

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
    
    for key, pattern in patterns.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            match = re.search(pattern, user_input, re.IGNORECASE)
            if key == "employees_in_department":
                department = match.group(1).strip()
                sql_query = "SELECT Name, Salary, Hire_Date FROM Employees WHERE Department = ?"
                params = (department,)
            elif key == "manager_of_department":
                department = match.group(1).strip()
                sql_query = "SELECT Manager FROM Departments WHERE Name = ?"
                params = (department,)
            elif key == "employees_hired_after":
                hire_date = match.group(1).strip()
                sql_query = "SELECT Name, Department, Hire_Date FROM Employees WHERE Hire_Date > ?"
                params = (hire_date,)
            elif key == "total_salary_expense":
                department = match.group(1).strip()
                sql_query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
                params = (department,)
            elif key == "employee_contact":
                name = match.group(1).strip()
                sql_query = "SELECT Email, Phone FROM Employees WHERE Name = ?"
                params = (name,)
            elif key == "employee_experience":
                name = match.group(1).strip()
                sql_query = "SELECT Experience FROM Employees WHERE Name = ?"
                params = (name,)
            elif key == "department_budget":
                department = match.group(1).strip()
                sql_query = "SELECT Budget FROM Departments WHERE Name = ?"
                params = (department,)
            elif key == "department_location":
                department = match.group(1).strip()
                sql_query = "SELECT Location FROM Departments WHERE Name = ?"
                params = (department,)
            elif key == "employees_by_position":
                position = match.group(1).strip()
                sql_query = "SELECT Name, Department FROM Employees WHERE Position = ?"
                params = (position,)
            elif key == "highest_paid_employee":
                sql_query = "SELECT Name, Salary FROM Employees ORDER BY Salary DESC LIMIT 1"
            elif key == "average_salary_department":
                department = match.group(1).strip()
                sql_query = "SELECT AVG(Salary) FROM Employees WHERE Department = ?"
                params = (department,)
            elif key == "employees_with_experience":
                experience = int(match.group(1).strip())
                sql_query = "SELECT Name, Department FROM Employees WHERE Experience > ?"
                params = (experience,)
            elif key == "employees_by_hire_year":
                hire_year = match.group(1).strip()
                sql_query = "SELECT Name, Department FROM Employees WHERE strftime('%Y', Hire_Date) = ?"
                params = (hire_year,)
            elif key == "specific_employee_details":
                name = match.group(1).strip()
                sql_query = "SELECT * FROM Employees WHERE Name = ?"
                params = (name,)
            elif key == "employees_by_email_domain":
                domain = match.group(1).strip()
                sql_query = "SELECT Name, Email FROM Employees WHERE Email LIKE ?"
                params = (f'%@{domain}',)
            break
    
    if sql_query:
        cursor.execute(sql_query, params)
        result = cursor.fetchall()
        conn.close()
        if result:
            return "\n".join([" | ".join(f"{col}: {val}" for col, val in zip([desc[0] for desc in cursor.description], row)) for row in result])
        return "I couldn't find the required data."
    
    conn.close()
    return "Sorry, I didn't understand your query. Please try again."

def chatbot_interface(user_input):
    return process_query(user_input)

iface = gr.Interface(
    fn=chatbot_interface,
    inputs=gr.Textbox(placeholder="Type your query..."),
    outputs="text",
    title="Natural Language SQL Query Assistant",
    description="Type your query in plain English and get database results.",
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()