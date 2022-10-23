def extract_chmi():
    from bs4 import BeautifulSoup

    with open(
        "/home/evzen/doc/script/python/fastapi/vedro/backend/static/files/chmi.html",
        "rb",
    ) as f:
        soup = BeautifulSoup(f, "html.parser")
        textik1 = soup.find_all("p", {"class": "textik1"})
        textik1 = [y.text for y in textik1]
        textik2 = soup.find_all("p", {"class": "textik2"})
        textik2 = [x.text for x in textik2]
        textik2 = [x.replace("\xa0", " ") for x in textik2]
        data = list(zip(textik1, textik2))
        return data
