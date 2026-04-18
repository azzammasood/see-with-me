"""
Mock PostgreSQL connection for architecture diagram and repo structure.
Handles user session data and state management.
"""
def get_db():
    # Stub for getting DB session
    return "DB_SESSION"

def get_user_profile(user_id: str):
    return {
        "user_id": user_id,
        "name": "Muhammad Jamil",
        "preferences": {"voice_feedback": True}
    }
