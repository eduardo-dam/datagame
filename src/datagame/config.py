import os

from dotenv import load_dotenv


def load_config() -> dict[str, str]:
    load_dotenv()

    riot_api_key = os.getenv("RIOT_API_KEY")

    if not riot_api_key:
        raise ValueError("RIOT_API_KEY não encontrada no .env")

    return {
        "riot_api_key": riot_api_key,
    }
