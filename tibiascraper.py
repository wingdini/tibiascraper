import requests
from bs4 import BeautifulSoup

char = 'thy lizard king'

url = "https://www.tibia.com/community/?subtopic=characters"
data = {"name" : char, "Submit.x" : "0", "Submit.y" : "0"}

content = requests.post(url, data).text

soup = BeautifulSoup(content, "html.parser")
tags = soup.find("div", class_="BoxContent").find_all("tr")

for tag in tags:
    if ":" in tag.text:
        split = tag.text.split(":")
        data[split[0]] = split[1]

data = {"subtopic" : "worlds", "world" : data["World"]}
content = requests.get("https://www.tibia.com/community/", data).text

soup = BeautifulSoup(content, "html.parser")
tags = soup.find_all("tr", class_="Odd")

for tag in tags:
    print(tag.text)