import requests
from bs4 import BeautifulSoup


url = (
    "https://www.chmi.cz/predpovedi/predpovedi-pocasi/ceska-republika/tydenni-predpoved"
)

page = requests.get(url)
with open(
    "/home/evzen/doc/script/python/fastapi/vedro/backend/static/files/chmi.html", "wb+"
) as f:
    f.write(page.content)
