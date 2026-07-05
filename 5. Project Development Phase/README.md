# Personalized Networking Assistant

## Project Overview

The Personalized Networking Assistant is an AI-powered web application that helps users generate personalized conversation starters for networking events. It analyzes event descriptions, extracts key themes, generates AI-based conversation suggestions, performs fact checking using the Wikipedia API, and stores conversation history and user feedback.

## Technologies Used

- Python
- FastAPI
- Streamlit
- DistilBERT
- GPT-2
- Wikipedia API
- Hugging Face Transformers

## Project Structure

```
app/
frontend/
tests/
requirements.txt
history.json
feedback.json
```

## Installation

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Backend

```bash
uvicorn app.main:app --reload
```

## Run the Frontend

```bash
streamlit run frontend/streamlit_app.py
```

## Features

- Event Theme Extraction
- AI Conversation Starter Generation
- Wikipedia Fact Checking
- Conversation History
- User Feedback Logging

## Team Members

- Virinchi
- M. Soma Sekhar
- Mude Dinesh Naik
- E. Vamsi Krishna