import requests

url = "https://www.in-pocasi.cz/"
page = requests.get(url)
with open("static/files/inpo.html", "wb+") as f:
    f.write(page.content)
