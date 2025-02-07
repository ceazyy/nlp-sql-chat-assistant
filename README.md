
# Natural Language SQL Query Assistant

This project is a chatbot-style assistant that allows users to interact with an SQLite database using natural language queries. It interprets user queries, converts them into SQL commands, executes them on the database, and returns relevant results in a user-friendly format.

## Features
- Converts plain English queries into SQL commands
- Retrieves employee and department data
- Supports a variety of queries such as salary calculations, employee details, and department information
- Provides structured output with column names for better readability
- Built using Python, SQLite, and Gradio

## Installation and Setup
### Prerequisites
- Python 3.x installed
- SQLite installed
- Required Python libraries

### Step 1: Clone the Repository
```
git clone https://github.com/your-username/nlp-sql-chat-assistant.git
cd nlp-sql-chat-assistant
```

### Step 2: Install Dependencies
```
pip install -r requirements.txt
```

### Step 3: Set Up the Database
Ensure that the SQLite database file (`employees.db`) is present inside the `database/` directory. If not, create and populate it using the provided SQL scripts.

### Step 4: Run the Application
```
python chatbot.py
```
This will launch a web-based interface where you can enter your queries.

## Usage
Users can type queries in natural language, and the assistant will process them to retrieve relevant database results. Some example queries include:

### Supported Queries
1. Show me all employees in the **[Department]** department
2. Who is the manager of the **[Department]** department?
3. List all employees hired after **[YYYY-MM-DD]**
4. What is the total salary expense for the **[Department]** department?
5. What is the contact information of **[Employee Name]**?
6. How much experience does **[Employee Name]** have?
7. What is the budget for the **[Department]** department?
8. Where is the **[Department]** department located?
9. List all **[Position]** in the company
10. Who is the highest-paid employee?
11. What is the average salary in the **[Department]** department?
12. List all employees with more than **[X]** years of experience
13. Who were hired in the year **[YYYY]**?
14. Give me details of **[Employee Name]**
15. List all employees with email domain **[domain.com]**

## Custom Queries
You can also enter free-form queries related to employees and departments. If the assistant cannot understand or find the requested data, it will return an appropriate message.

