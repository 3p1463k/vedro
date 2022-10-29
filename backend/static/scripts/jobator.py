import os
import schedule
from time import sleep

# from scrape_chmi import chmiscrape
from parse_chmi import make_df

print("Startin jobator ... ")


def job1():

    chmiscrape()


def job2():

    print("Creating data frame ...")

    make_df()

    print("All done, quitting ...")


# schedule.every().day.at("15:40").do(job2)
# schedule.every(60).minutes.do(job2)
# schedule.every(10).seconds.do(job3)
# schedule.every(1).minute.do(job1)
# schedule.every(5).seconds.do(job10)

# schedule.every(220).minutes.do(job1)
schedule.every(2).minutes.do(job2)

while 1:
    schedule.run_pending()
    sleep(1)
