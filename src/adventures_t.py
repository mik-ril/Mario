import time
import logging

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from src.utility import wait

def check_adventures(
        driver: uc.Chrome
):
    try:
        button=driver.find_element(By.CSS_SELECTOR, 'a[class="directLink adventureLink clickable"]')
        return button
    except:
        logging.warning("No adventure available")
        return None

def check_health(
        driver: uc.Chrome
):
    bar=driver.find_element(By.CSS_SELECTOR, 'div[class="health progressbar"]')
    perc=int(str(bar.get_attribute('perc')).encode('ascii','ignore'))
    return perc

def start_adventure(
        driver: uc.Chrome,
        adventures
):
    adventures.click()
    wait()
    button=driver.find_element(By.CSS_SELECTOR, 'button[clickable="acceptQuest()"]')
    if str(button.get_attribute('class'))=='animate clickable disabled':
        logging.warning("Hero not available for adventure")
    else:
        button.click()
        logging.warning("... the hero is on their way!")
    wait()
    driver.find_element(By.CSS_SELECTOR, 'a[clickable="closeWindow(\'hero\')"]').click()

def thread_adventures(
        lock,
        driver:   uc.Chrome,
        health:   int,
        interval: int
):
    while True:
        lock.acquire()

        logging.warning("Looking for an adventure...")
        adventures=check_adventures(driver)
        res_health=check_health(driver)
        if res_health>health:
            start_adventure(driver, adventures)
        else:
            logging.warning("Not enough health")

        lock.release()
        time.sleep(interval)