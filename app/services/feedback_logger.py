# app/services/feedback_logger.py

import json
from datetime import datetime
from pathlib import Path

FEEDBACK_FILE = Path("feedback.json")


def log_feedback(suggestion: str, action: str):
    """
    Save user feedback (like/dislike) into feedback.json
    """

    feedback_entry = {
        "suggestion": suggestion,
        "action": action,
        "timestamp": datetime.now().isoformat()
    }

    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r") as f:
            feedback = json.load(f)
    else:
        feedback = []

    feedback.append(feedback_entry)

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedback, f, indent=2)


def load_feedback():
    """
    Load all feedback entries.
    """

    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)

    return []