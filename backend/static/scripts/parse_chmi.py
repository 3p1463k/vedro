def extract_chmihtml():
    from bs4 import BeautifulSoup

    print("Extracting html")

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


def extrac_chmi_strings():
    import pandas as pd
    import numpy as np

    print("Extracting chmi strings")

    firs = np.array([])
    sec = np.array([])
    temps = np.array([])
    titls = np.array([])
    h = np.array([])
    l = np.array([])
    vitr = np.array([])

    data = extract_chmihtml()

    for x in data:
        from nltk import tokenize

        title = x[0]
        if "(00-24)" in title:
            title = title.replace("(00-24)", "")
        else:
            pass

        cont = x[1]
        f1 = tokenize.sent_tokenize(cont)[0:1]
        f2 = tokenize.sent_tokenize(cont)[1:2]
        r2 = tokenize.sent_tokenize(cont)[2::]

        firs = np.append(firs, f1)
        sec = np.append(sec, f2)
        temps = np.append(temps, r2)
        titls = np.append(titls, title)

    for k in temps:
        if "Nejnižší" in k:
            l = np.append(l, k)

        elif "Nejvyšší" in k:
            h = np.append(h, k)

        elif "vítr" in k:
            vitr = np.append(vitr, k)

        else:
            pass

    newcontent = list(zip(titls[1::], firs[1::], sec[1::], l, h, vitr))

    return newcontent


def make_df():
    import pandas as pd

    newcontent = extrac_chmi_strings()
    df = pd.DataFrame(
        newcontent, columns=["Day", "First", "Sec", "Low", "High", "Wind"]
    )

    df.to_csv(
        "/home/evzen/doc/script/python/fastapi/vedro/backend/static/files/chmidf.csv",
        index=False,
    )

    return df
