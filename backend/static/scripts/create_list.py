import pandas as pd
import numpy as np


def make_list():
    # Read data
    df = pd.read_csv("static/files/chmidf.csv")

    nvitr = np.array([])
    # search data for wind speeds and create column wind
    for x in df["Wind"]:

        new = x.split("vítr")[1].split("m/s")[0].strip()[-2::]
        nvitr = np.append(nvitr, new)

    df["wind"] = [int(j) for x in nvitr for j in x if j.isdigit()]
    # search for lowest and highest temperatures and create column
    z = [x.split(",")[0] for x in df["Low"]]
    low = list(
        zip(
            [(int(j)) for x in z for j in x.split() if j.isdigit()][::2],
            [(int(j)) for x in z for j in x.split() if j.isdigit()][1::2],
        )
    )
    df["Templow"] = low
    df["Temphigh"] = list(
        zip(
            [
                int(j)
                for k in [
                    x.split("teploty", 1)[1].split(",")[0].split() for x in df.High
                ]
                for j in k
                if j.isdigit()
            ][::2],
            [
                int(j)
                for k in [
                    x.split("teploty", 1)[1].split(",")[0].split() for x in df.High
                ]
                for j in k
                if j.isdigit()
            ][1::2],
        )
    )

    df1 = df.iloc[:, [0, 6]].copy()
    # create simpler data frame and list  for feeding data to app
    df1["lohi"] = list(zip(*df.Templow))[0]
    df1["lolo"] = list(zip(*df.Templow))[1]
    df1["hilo"] = list(zip(*df.Temphigh))[0]
    df1["hihi"] = list(zip(*df.Temphigh))[1]
    df1["avglo"] = (df1.lolo + df1.hilo) / 2
    df1["avghi"] = (df1.hilo + df1.hihi) / 2

    mylist = [row for row in df1.itertuples()]

    return mylist
