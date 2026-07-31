from Database import DBHelper

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')


def list_tasks(filters=None):

    if filters is None:
        filters = {}

    tasks = db_helper.find(filters)

    active_filters = {
    key: value
    for key, value in filters.items()
    if value not in (None, "", [])
    }

    if len(tasks) == 0:

        # if active_filters:
        #     return "📭 No tasks match your request."

        return (
            "📭 Your task list is empty.\n\n"
            "You're all caught up! 🎉"
        )

    result = "📋 **Your Tasks**\n\n"

    for index, task in enumerate(tasks, start=1):

        result += (
            f"**{index}. {task['title']}**\n\n"
            f"👤 Contact : {task.get('name', 'N/A')}\n\n"
            f"📝 Description : {task['description']}\n\n"
            f"⚡ Action : {task['action']}\n\n"
            f"📌 Status : {task['status']}\n\n"
        )

    return result