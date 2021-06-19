import requests

response = requests.get("https://i.imgur.com/ExdKOOz.png")

open("C:/Users/Shawn/Desktop/ygopic/sampuru.png", "wb")
file.write(response.content)
file.close()
