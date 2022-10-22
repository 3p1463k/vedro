from bs4 import BeautifulSoup

with open(
    "/home/evzen/doc/script/python/fastapi/vedro/backend/static/files/chmip.html", "rb"
) as f:
    soup = BeautifulSoup(f, "html.parser")
    all_ps = soup.find_all("p")
    for x in all_ps:
        print(x.text)
