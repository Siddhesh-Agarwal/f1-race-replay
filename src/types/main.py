from enum import Enum
from typing import Literal, Dict, Any, List, TypedDict, Tuple

TyreType = Literal["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"]


class SessionType(str, Enum):
    RACE = "R"
    SPRINT = "S"
    QUALIFYING = "Q"
    SPRINT_QUALIFYING = "SQ"


class QualiTelemetryResult(TypedDict):
    code: str
    position: int
    color: Tuple[int, int, int]
    Q1: str | None
    Q2: str | None
    Q3: str | None


class QualiTelemetry(TypedDict):
    results: List[QualiTelemetryResult]
    telemetry: Dict[str, Any]
    max_speed: float
    min_speed: float
