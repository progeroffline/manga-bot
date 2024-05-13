import requests
from environs import Env
env = Env()
env.read_env()
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")

domain = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

get_me = f"{domain}/getMe"

response = requests.get(get_me)

json_response = response.json()["result"]
name = json_response["first_name"]
username = json_response["username"]

print()
