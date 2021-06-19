import requests

response = requests.get("https://i.imgur.com/ExdKOOz.png")

file = open("C:/Users/Shawn/Desktop/ygopic/sampuru.png", "wb")
file.write(response.content)
file.close()
