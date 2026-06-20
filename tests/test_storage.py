import json

from datagame.storage import save_json


def test_save_json_creates_file_with_expected_data(tmp_path) -> None:
    players = [
        {"name": "Jogador 1", "tier": "BRONZE"},
        {"name": "Jogador 2", "tier": "SILVER"},
    ]

    file_path = tmp_path / "players.json"

    save_json(players, file_path)

    assert file_path.exists()

    with file_path.open("r", encoding="utf-8") as file:
        saved_players = json.load(file)

    assert saved_players == players
