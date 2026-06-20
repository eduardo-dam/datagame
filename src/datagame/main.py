from datagame.config import load_config
from datagame.riot_api import get_league_entries
from datagame.storage import save_json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent


def main() -> None:
    config = load_config()

    players_list = get_league_entries(
        api_key=config["riot_api_key"],
        tier="BRONZE",
        division="IV",
        queue="RANKED_SOLO_5x5",
        page=1,
    )

    file_path = project_root / "data" / "cache" / "players" / "bronze_players.json"
    save_json(players_list, file_path)

    print(players_list)


if __name__ == "__main__":
    main()
