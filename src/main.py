from config import load_config
from riot_api import get_match_ids, get_puuid

def main() -> None:
  config = load_config()

  game_name = "Uliheit01"
  tag_line = "br1"

  puuid = get_puuid(
    api_key = config["riot_api_key"],
    game_name = game_name,
    tag_line = tag_line,

  )

  match_ids = get_match_ids(
    api_key = config["riot_api_key"],
    puuid=puuid,
    count=5
  )

  print(match_ids)

if __name__ == "__main__":
  main()