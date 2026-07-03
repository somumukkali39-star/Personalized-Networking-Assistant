# app/routers/conversation.py

from fastapi import APIRouter

from app.models.schemas import (
    EventInput,
    ConversationRequest,
    ConversationResponse,
    FactCheckRequest,
    FactCheckResponse,
)

from app.services.event_analyzer import extract_event_themes
from app.services.topic_generator import generate_topics
from app.services.fact_checker import fact_check
from app.services.history_logger import log_conversation

router = APIRouter()


@router.post("/analyze-event")
def analyze_event(request: EventInput):

    topics = extract_event_themes(request.description)

    return {
        "topics": topics
    }


@router.post(
    "/fact-check",
    response_model=FactCheckResponse
)
def verify_fact(request: FactCheckRequest):

    summary = fact_check(request.query)

    return FactCheckResponse(summary=summary)


@router.post(
    "/generate-conversation",
    response_model=ConversationResponse
)
def generate_conversation(request: ConversationRequest):

    topics = extract_event_themes(request.description)

    suggestions = generate_topics(
        topics,
        request.interests
    )

    log_conversation({
        "description": request.description,
        "interests": request.interests,
        "topics": topics,
        "suggestions": suggestions
    })

    return ConversationResponse(
        topics=topics,
        suggestions=suggestions
    )