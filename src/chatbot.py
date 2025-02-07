import gradio as gr
from query_engine import process_query

def chatbot_interface(user_input):
    response = process_query(user_input)
    if isinstance(response, list) and response:
        if "employees in" in user_input.lower():
            formatted_response = "\n".join([f"Name: {row[0]}, Salary: {row[1]}, Hire Date: {row[2]}" for row in response])
        elif "manager of" in user_input.lower():
            formatted_response = f"Manager: {response[0][0]}"
        elif "hired after" in user_input.lower():
            formatted_response = "\n".join([f"Name: {row[0]}, Department: {row[1]}, Hire Date: {row[2]}" for row in response])
        elif "total salary expense" in user_input.lower():
            formatted_response = f"Total Salary Expense: {response[0][0]}"
        else:
            formatted_response = "\n".join([", ".join(map(str, row)) for row in response])
        return formatted_response
    return response

iface = gr.Interface(
    fn=chatbot_interface,
    inputs=gr.Textbox(placeholder="Ask a database question..."),
    outputs="text",
    title="Natural Language SQL Query Assistant",
    description="Type your query in plain English and get database results.",
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()
