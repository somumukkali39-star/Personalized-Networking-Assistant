# app/services/topic_generator.py

from transformers import pipeline, set_seed
from app.config import MODEL_NAMES

# Load GPT-2 once
generator = pipeline(
    "text-generation",
    model=MODEL_NAMES["text_generator"]
)

# For reproducible results
set_seed(42)


def generate_topics(event_themes, user_interests):
    """
    Generate conversation starters based on event themes and user interests.
    """

    prompt = (
        f"I'm attending a networking event focused on {', '.join(event_themes)}. "
        f"I'm personally interested in {', '.join(user_interests)}. "
        f"Generate three short and engaging professional conversation starters."
    )

    outputs = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        do_sample=True
    )

    generated_text = outputs[0]["generated_text"]

    # Remove the prompt from the generated text
    generated_text = generated_text.replace(prompt, "").strip()

    # Split into separate suggestions
    suggestions = [
        line.strip("-• ").strip()
        for line in generated_text.split("\n")
        if line.strip()
    ]

    # If GPT-2 returns everything in one paragraph,
    # provide a fallback.
    if len(suggestions) == 0:
        suggestions = [generated_text]

    return suggestions[:3]