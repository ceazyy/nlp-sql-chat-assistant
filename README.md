
# Natural Language SQL Query Assistant

This project is a chatbot-based assistant that enables users to query an SQLite database using natural language. It translates user input into SQL queries, executes them, and returns structured results in an easy-to-read format.

## Features
- Converts plain English queries into SQL statements
- Retrieves employee and department details
- Supports salary calculations, hiring dates, managerial information, and more
- Displays well-structured results with relevant column names
- Developed using Python, SQLite, and Gradio

## Installation and Setup
### Prerequisites
- Python 3.x installed
- SQLite installed
- Required Python dependencies

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/nlp-sql-chat-assistant.git
cd nlp-sql-chat-assistant
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure the Database
Ensure that the SQLite database file (`employees.db`) is located inside the `database/` directory. If it is missing, create and populate it using the provided SQL scripts.

### Step 4: Run the Application
```bash
python chatbot.py
```
This will launch a web-based interface where you can enter your queries in natural language.

## Usage
Simply type your query, and the assistant will process it to return relevant results from the database.

### Example Queries
1. Show me all employees in the **[Department]** department
2. Who is the manager of the **[Department]** department?
3. List all employees hired after **[YYYY-MM-DD]**
4. What is the total salary expense for the **[Department]** department?
5. What is the contact information of **[Employee Name]**?
6. How much experience does **[Employee Name]** have?
7. What is the budget for the **[Department]** department?
8. Where is the **[Department]** department located?
9. List all **[Position]** in the company
10. Who is the highest paid employee?
11. What is the average salary in the **[Department]** department?
12. List all employees with more than **[X]** years of experience
13. Who were hired in the year **[YYYY]**?
14. Provide details of **[Employee Name]**
15. List all employees with email domain **[domain.com]**

## Custom Queries
Users can enter free-form queries related to employees and departments. If the system does not recognize or find the requested data, it will return an appropriate message.
