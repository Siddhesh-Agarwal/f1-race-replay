from typing import Dict, Union, Literal
from src.types import TyreType

tyre_compounds_ints: Dict[TyreType, int] = {
    "SOFT": 0,
    "MEDIUM": 1,
    "HARD": 2,
    "INTERMEDIATE": 3,
    "WET": 4,
}


def get_tyre_compound_int(compound_str: TyreType) -> int:
    return tyre_compounds_ints.get(compound_str, -1)


def get_tyre_compound_str(compound_int: int) -> Union[TyreType, Literal["UNKNOWN"]]:
    for k, v in tyre_compounds_ints.items():
        if v == compound_int:
            return k
    return "UNKNOWN"
