from Database import DBHelper
from config import openai_client
import datetime
import json

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')

def save_task(task):
    # Adding 2 more keys in task
    task['status'] = 'pending'
    task['created_at'] = datetime.datetime.now()
    db_helper.save(task)
     
    result=(
        f"Task saved successfully as **pending** \n\n",
        f"**Action** {task['action']} \n\n",
        f"**Title** {task['title']} \n\n",
        f"**Description** {task['description']} \n\n"
    )
     
    return result

# 2. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "name": "save_task",
        "description": "Save the task in MongoDB Atlas which a user will write",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the Task",
                },
                "description": {
                    "type": "string",
                    "description": "Description of the Task",
                },
                "action": {
                    "type": "string",
                    "enum": ["call","message","email","Other"],
                    "description": "Action of the Task can be call, message or email",
                },
            },
            "required": ["title", "description", "action"],
        },
    },
]

def agentic_save(input_list):
    # Prompt the model with tools defined
    response = openai_client.responses.create(
        model="gpt-4o-mini",
        tools=tools,
        input=input_list,
    )  

    llm_output = response.model_dump_json(indent=2) # string
    print(llm_output)
    llm_output = json.loads(llm_output) # covert to dictionary
    result = 'Sorry, I cannot process your request'

    output_type = llm_output['output'][0]['type']

    if output_type == 'function_call':
        arguments = json.loads(llm_output['output'][0]['arguments'])
        function_name = llm_output['output'][0]['name']

        if function_name == 'save_task':
            arguments['user_original_input'] = input_list[0]['content']
            result = save_task(arguments)
        elif function_name == 'update_task':
            pass
        elif function_name == 'delete_task':
            pass
        elif function_name == 'list_tasks':
            pass
    return result