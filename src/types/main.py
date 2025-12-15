from enum import Enum
from typing import Literal, Dict, Any, List, TypedDict, Tuple, Optional

TyreType = Literal["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"]


class SessionType(str, Enum):
    RACE = "R"
    SPRINT = "S"
    QUALIFYING = "Q"
    SPRINT_QUALIFYING = "SQ"


DriverColor = Tuple[int, int, int]


class RaceTelemetryTrackStatus(TypedDict):
    status: str
    start_time: float
    end_time: Optional[float]


class RaceTelemetry(TypedDict):
    frames: List[Any]
    driver_colors: Dict[str, DriverColor]
    track_statuses: List[RaceTelemetryTrackStatus]
    total_laps: int


class QualiTelemetryResult(TypedDict):
    code: str
    position: int
    color: DriverColor
    Q1: str | None
    Q2: str | None
    Q3: str | None


class QualiTelemetry(TypedDict):
    results: List[QualiTelemetryResult]
    telemetry: Dict[str, Any]
    max_speed: float
    min_speed: float


class WeatherSnapshot(TypedDict):
    track_temp: float | None
    air_temp: float | None
    humidity: float | None
    wind_speed: float | None
    wind_direction: float | None
    rain_state: Literal["DRY", "RAINING"]
