# models.py
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class SummaryRequest(BaseModel):
    text: str = Field(min_length=50, max_length=50_000)
    style: Literal["bullet", "paragraph"] = "paragraph"


class SummaryResponse(BaseModel):
    summary: str
    key_points: list[str] = Field(max_length=10)
    confidence: float = Field(ge=0, le=1)

    @field_validator("summary")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("empty summary")
        return v


# Validating raw LLM output:
raw = '{"summary": "...", "key_points": ["a"], "confidence": 0.8}'
result = SummaryResponse.model_validate_json(raw)
