import requests

url = "https://ai-draw-discord-bot.glitch.me/status"
response = requests.get(url)
print(response.text)
