from elevenlabs.environment_variables.types import update_environment_variable_request_values_value
from Database import DBHelper

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')


def update_task(title, updates):

    result = db_helper.update(
        condition={"title": title},
        document_to_update=updates
    )

    if result.matched_count == 0:
        return (
            f"❌ No task found with title '{title}'."
        )

    if result.modified_count == 0:
        return (
            f"ℹ️ Task '{title}' is already up-to-date."
        )

    updated_fields = ", ".join(updates.keys())

    changes = "\n".join(
    [f"• {key}: {value}" for key, value in updates.items()]
)

    return (
        f"✅ Task updated successfully!\n\n"
        f"📌 Task: **{title}**\n\n"
        f"Changes Made:\n{changes}"
    )