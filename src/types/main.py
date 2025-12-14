from enum import Enum
from typing import Literal

TyreType = Literal["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"]


class SessionType(str, Enum):
    RACE = "R"
    SPRINT = "S"
    QUALIFYING = "Q"
    SPRINT_QUALIFYING = "SQ"
