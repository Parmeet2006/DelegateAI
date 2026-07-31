from Database import DBHelper

db_helper = DBHelper()
db_helper.select_collection("tasks")


def dashboard_stats():

    pending = db_helper.count({"status": "pending"})
    completed = db_helper.count({"status": "completed"})
    total = db_helper.count()

    calls = db_helper.count({
        "status": "pending",
        "action": "call"
    })

    emails = db_helper.count({
        "status": "pending",
        "action": "email"
    })

    messages = db_helper.count({
        "status": "pending",
        "action": "message"
    })

    return {
        "pending": pending,
        "completed": completed,
        "total": total,
        "calls": calls,
        "emails": emails,
        "messages": messages
    }