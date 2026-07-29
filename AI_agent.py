from Database import DBHelper
from config import openai_client
import datetime
import json
from Pages.Update_task import update_task
from Pages.Delete_task import delete_task
from Pages.List_task import list_tasks

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')

def save_task(task):
    # Adding 2 more keys in task
    task['status'] = 'pending'
    task['created_at'] = datetime.datetime.now()
    db_helper.save(task)
     
    result = (
        f"Task saved successfully as **pending**\n\n"
        f"**Title:** {task['title']}\n\n"
        f"**Contact Name:** {task.get('name', 'N/A')}\n\n"
        f"**Description:** {task['description']}\n\n"
        f"**Action:** {task['action']}"
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
                "name": {
                    "type": "string",
                    "description": "Name of the contact person",
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
    {
        "type": "function",
        "name": "update_task",
        "description": "Update an existing task by modifying one or more fields like title, description, contact name, action or status.",
        "parameters": {
            "type": "object",
            "properties": {

                "title": {
                    "type": "string",
                    "description": "The exact title of the existing task stored in the database that should be updated. Preserve the title exactly as it was originally created."
                },

                "updates": {
                    "type": "object",
                    "description": "Fields that need updating.",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "action": {
                            "type": "string",
                            "enum": ["call","message","email","Other"]
                        },
                        "status": {
                            "type": "string",
                            "enum": ["pending","calling","completed","failed"]
                        }
                    }
                }
            },
            "required": ["title","updates"]
        }
    },
    {
        "type": "function",
        "name": "delete_task",
        "description": "Delete an existing task from MongoDB using its exact title.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The exact title of the task to delete."
                }
            },
            "required": ["title"]
        }
    },
    {
        "type": "function",
        "name": "list_tasks",
        "description": "Retrieve tasks from MongoDB. Filters are optional.",
        "parameters": {
            "type": "object",
            "properties": {
                "filters": {
                    "type": "object",
                    "properties": {
                        "status": {
                        "type": "string",
                        "enum": ["pending","calling","completed","failed"]
                    },

                    "action": {
                        "type": "string",
                        "enum": ["call","message","email","Other"]
                        }

                    }
                }

            }  
        }
    }
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
        
        elif function_name == "update_task":
            result = update_task(
                title=arguments["title"],
                updates=arguments["updates"])
        
        elif function_name == 'delete_task':
            result = delete_task(title=arguments["title"])

        elif function_name == 'list_tasks':
            filters = arguments.get("filters", {})
            result = list_tasks(filters)
    
    return result