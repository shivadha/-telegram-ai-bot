user_sessions = {}

def get_session(user_id):
    if user_id not in user_sessions:
        user_sessions[user_id] = {
            "state": "idle",
            "data": {}
        }
    return user_sessions[user_id]

def update_state(user_id, new_state):
    user_sessions[user_id]["state"] = new_state
