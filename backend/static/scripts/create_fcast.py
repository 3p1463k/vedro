import pandas as pd


def make_list1():
    df2 = pd.read_csv("static/files/chmidf.csv")
    mylist1 = list(zip(df2["Day"], df2["First"], df2["Sec"]))

    return mylist1
