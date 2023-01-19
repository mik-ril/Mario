import time
import logging

import undetected_chromedriver as uc

from src.troops import send_troops

def read_farmlist():
    with open('farmlist.txt') as file:
        farmlist=[[int(x) for x in line.split()] for line in file]
    return farmlist

def thread_farming(
        lock,
        driver:   uc.Chrome,
        village:  int,
        troops:   list,
        interval: int
):
    while True:
        lock.acquire()

        logging.warning(f"Starting farmlist in {village}...")
        farmlist=read_farmlist()

        for farm in farmlist:
            send_troops(driver, village, farm, troops, 2)

        lock.release()
        time.sleep(interval)