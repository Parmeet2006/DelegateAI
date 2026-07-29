from Database import DBHelper

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')


def delete_task(title):

    result = db_helper.delete(
        condition={"title": title}
    )

    if result.deleted_count == 0:
        return (
            f"❌ No task found with title '{title}'."
        )

    return (
        f"🗑️ Task deleted successfully!\n\n"
        f"Deleted Task:\n"
        f"• {title}"
    )