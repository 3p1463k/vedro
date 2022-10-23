def extract_inpo():
    from bs4 import BeautifulSoup
    import pandas as pd

    with open(
        "/home/evzen/doc/script/python/fastapi/vedro/backend/static/files/inpo.html",
        "rb",
    ) as f:
        soup = BeautifulSoup(f, "html.parser")

    days = soup.find_all("div", {"class": "day"})
    tex = [y.text for y in days]
    daynames = [x[0:-7].strip()[0:-2] for x in tex]
    daytemps = [x[0:-7].strip()[-2:] for x in tex]
    df = pd.DataFrame({"Day": daynames, "Temp": daytemps})
    df["Temp"] = df["Temp"].astype(int)
    data = list(zip(daynames, daytemps))
    return data
