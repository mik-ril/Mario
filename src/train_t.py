import time
import logging

import undetected_chromedriver as uc

from src.train import train_troops
def thread_train(
        lock,
        driver:   uc.Chrome,
        tribe:    int,
        village:  int,
        troops:   list,
        interval: int
):
    while True:
        lock.acquire()

        logging.warning(f"Training troops in {village}...")
        train_troops(driver, tribe, village, troops)

        lock.release()
        time.sleep(interval)