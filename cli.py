from enum import Enum
from typing import Annotated

from typer import Typer, Argument
from app.main import run_api_app

cli = Typer(help="Delivery Service CLI")

class Apps(str, Enum):
    api = "api"

@cli.command(help="Run API app")
def run(
    app: Annotated[Apps, Argument(help="App to run")] = Apps.api
):
    match app:
        case Apps.api:
            run_api_app()

cli()
