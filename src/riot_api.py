import requests

ACCOUNT_BASE_URL = "https://americas.api.riotgames.com"

def _raise_for_riot_error(response: requests.Response) -> None:
  if response.status_code == 401:
    raise ValueError("API Key inválida ou expirada")
  
  if response.status_code == 403:
    raise ValueError("API key sem permissão para acessar a Riot API.")

  if response.status_code == 404:
    raise ValueError("Recurso não encontrado na Riot API.")
  
  if response.status_code == 429:
    raise ValueError("Rate limit atingido na Riot API.")
  
  response.raise_for_status()

def get_puuid(api_key: str, game_name: str, tag_line: str) -> str:
  url = (
      f"{ACCOUNT_BASE_URL}/riot/account/v1/accounts/by-riot-id/"
      f"{game_name}/{tag_line}"
  )
  hearders = {"X-Riot-Token": api_key}
  response = requests.get(url, headers=hearders, timeout=30)
  _raise_for_riot_error(response)

  account_data = response.json()

  if "puuid" not in account_data:
    raise ValueError("Resposta da Riot API não contém puuid.")

  return account_data["puuid"]

def get_match_ids(api_key: str, puuid: str, count: int = 5) -> list[str]:
  url = (
    f"{ACCOUNT_BASE_URL}/lol/match/v5/matches/by-puuid/"
    f"{puuid}/ids"
  )
  hearders = {"X-Riot-Token":api_key}
  params = {"start": 0, "count": count}
  response = requests.get(url, headers=hearders, params=params, timeout=30)
  _raise_for_riot_error(response)

  match_ids = response.json()

  if not isinstance(match_ids, list):
    raise ValueError("Resposta da Riot API não tem partidas.")
  
  return match_ids
