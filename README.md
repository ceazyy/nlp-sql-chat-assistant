# Natural Language SQL Query Assistant

This project is a chatbot-based assistant that allows users to interact with an SQLite database using natural language queries. The assistant translates user input into SQL queries, executes them, and returns structured results in an easy-to-read format.

## How It Works
1. The user enters a query in plain English.
2. The chatbot processes the input and matches it with predefined patterns.
3. If a match is found, the system generates a corresponding SQL query.
4. The query is executed on the SQLite database.
5. The assistant retrieves and formats the results before displaying them to the user.
6. If the query is not recognized, an appropriate error message is returned.

## Features
- Converts plain English queries into SQL commands
- Retrieves employee and department details
- Supports queries related to salaries, hiring dates, managers, and more
- Provides structured and readable results
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
This will launch a web-based interface where you can enter queries in natural language.

## Usage
Simply type a query, and the assistant will process it to return relevant results from the database.

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
14. Give me details of **[Employee Name]**
15. List all employees with email domain **[domain.com]**

## Known Limitations
- The assistant relies on predefined query patterns and may not handle complex or ambiguous queries effectively.
- The system does not support advanced SQL operations such as joins, subqueries, or nested queries.
- If a query does not match any predefined pattern, it returns a generic error message.
- Data accuracy depends on the correctness of the SQLite database entries.

## Suggestions for Improvement
- Implement LLM techniques to improve query recognition.
- Expand the range of supported queries and improve flexibility.
- Add support for more complex SQL operations like joins and nested queries.
- Improve error handling and response messages for better user experience.

