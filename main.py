from typing import Annotated
import typer
from src.f1_data import (
    get_race_telemetry,
    enable_cache,
    get_circuit_rotation,
    load_session,
    get_quali_telemetry,
)
from src.arcade_replay import run_arcade_replay
from src.interfaces.qualifying import run_qualifying_replay
from src.types import SessionType


app = typer.Typer()


@app.command()
def main(
    year: Annotated[int, typer.Option("--year", "-y", help="F1 season year")] = 2025,
    round_number: Annotated[
        int, typer.Option("--round", "-r", help="Race round number")
    ] = 12,
    playback_speed: Annotated[
        float, typer.Option("--speed", "-s", help="Playback speed multiplier")
    ] = 1.0,
    session_type: Annotated[
        SessionType, typer.Option("--session", "-t", help="Session type")
    ] = SessionType.RACE,
    chart: Annotated[
        bool, typer.Option("--chart", help="Enable chart display")
    ] = False,
    sprint: Annotated[
        bool, typer.Option("--sprint", help="Sprint race session")
    ] = False,
    qualifying: Annotated[
        bool, typer.Option("--qualifying", "-q", help="Qualifying session")
    ] = False,
    sprint_qualifying: Annotated[
        bool,
        typer.Option("--sprint-qualifying", "--sq", help="Sprint qualifying session"),
    ] = False,
):
    """Run F1 session replay with arcade-style visualization."""

    # Handle legacy flag-based session type selection
    if sprint_qualifying:
        session_type = SessionType.SPRINT_QUALIFYING
    elif sprint:
        session_type = SessionType.SPRINT
    elif qualifying:
        session_type = SessionType.QUALIFYING
    else:
        session_type = SessionType.RACE

    typer.echo(f"Loading F1 {year} Round {round_number} Session '{session_type.value}'")

    session = load_session(year, round_number, session_type)

    typer.echo(
        f"Loaded session: {session.event['EventName']} - "
        f"{session.event['RoundNumber']} - {session_type.value}"
    )

    enable_cache()

    if session_type in (SessionType.QUALIFYING, SessionType.SPRINT_QUALIFYING):
        qualifying_session_data = get_quali_telemetry(
            session, session_type=session_type
        )

        title = (
            f"{session.event['EventName']} - "
            f"{'Sprint Qualifying' if session_type == SessionType.SPRINT_QUALIFYING else 'Qualifying Results'}"
        )

        run_qualifying_replay(
            session=session,
            data=qualifying_session_data,
            title=title,
        )
    else:
        race_telemetry = get_race_telemetry(session, session_type=session_type)
        fastest_lap = session.laps.pick_fastest()
        if fastest_lap is None:
            raise ValueError("No fastest lap found")
        example_lap = fastest_lap.get_telemetry()
        drivers = session.drivers
        circuit_rotation = get_circuit_rotation(session)

        run_arcade_replay(
            frames=race_telemetry["frames"],
            track_statuses=race_telemetry["track_statuses"],
            example_lap=example_lap,
            drivers=drivers,
            playback_speed=playback_speed,
            driver_colors=race_telemetry["driver_colors"],
            title=f"{session.event['EventName']} - {'Sprint' if session_type == SessionType.SPRINT else 'Race'}",
            total_laps=race_telemetry["total_laps"],
            circuit_rotation=circuit_rotation,
            chart=chart,
        )


if __name__ == "__main__":
    app()
