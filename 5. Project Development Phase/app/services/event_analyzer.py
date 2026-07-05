# app/services/event_analyzer.py

from transformers import pipeline
from app.config import MODEL_NAMES

# Load the model once when the application starts
classifier = pipeline(
    "zero-shot-classification",
    model=MODEL_NAMES["event_analysis"]
)


def extract_event_themes(description: str, candidate_labels=None):
    """
    Extract the top 3 themes from an event description.
    """

    if candidate_labels is None:
        candidate_labels = [
            "AI",
            "Healthcare",
            "Blockchain",
            "Education",
            "Sustainability",
            "Finance",
            "Cybersecurity",
            "Cloud Computing",
            "Machine Learning",
            "Robotics"
        ]

    result = classifier(description, candidate_labels)

    return result["labels"][:3]