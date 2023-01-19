import time
import logging

from src.village import *
from src.troops import send_troops

def check_robbers(
        driver:  uc.Chrome,
        village: int
):
    open_village(driver,village)
    open_map(driver)
    robbers=driver.find_elements(By.CSS_SELECTOR, 'div[class="villageName unselectable robber"]')
    return robbers


def thread_robbers(
        lock,
        driver: uc.Chrome,
        village: int,
        troops: list,
        mode: int,
        interval: int
):
    while True:
        lock.acquire()

        logging.warning("Looking for robbers...")
        robbers = check_robbers(driver, village)
        if len(robbers):
            robbers[0].click()
            wait()
            driver.find_element(By.CSS_SELECTOR, 'i[class="feature_sendTroops_medium_illu"]').click()
            send_troops(driver, None, None, troops, mode)

        else:
            logging.warning("We already slayed every robber!")

        lock.release()
        time.sleep(interval)