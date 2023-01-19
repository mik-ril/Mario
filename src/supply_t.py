import time
import logging

import undetected_chromedriver as uc

from src.merchants import send_resources
def thread_supply(
        lock,
        driver: uc.Chrome,
        source:   int,
        target:   list,
        quantity: list,
        interval: int
):
    while True:
        lock.acquire()

        if target[0]!=None:
            logging.warning(f"Trying to send resources from {source} to ({target[0]}|{target[1]})...")
        else:
            logging.warning(f"Trying to send resources from {source} to {target[1]}...")
        send_resources(driver, source, target, quantity)

        lock.release()
        time.sleep(interval)