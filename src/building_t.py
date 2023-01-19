import time
import logging

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from src.utility import wait
from src.village import *

def thread_building(
        lock,
        driver:    uc.Chrome,
        buildings: list,
        interval:  int
):
    while True:
        lock.acquire()

        for building in buildings:
            logging.warning(f"Trying to build slot {building[1]} in village {building[0]}, up to level {building[2]}")
            open_village(driver,building[0])

            if building[1]<19:
                open_village_resources(driver)
            else:
                open_village_city(driver)

            open_building(driver, building[1])
            try:
                button=driver.find_element(By.XPATH,'/html/body/div[3]/window/div/div/div[3]/div/span/div/div')
                ActionChains(driver).move_to_element(button).perform()
                wait()

                label=button.find_element(By.CSS_SELECTOR,'span[class="buildingLevel"]')
                level=int(label.get_attribute('innerHTML').encode('ascii','ignore'))

                #problem: while something is being constructed, even if there is a free slot AND
                #the bubble is green, the object becomes "buildingBubble clickable disabledHover"
                #and it cannot be clicked -> .click() does not have effect
                #why in the bloody hell?

                if level>=building[2]:
                    logging.warning("Level already reached")
                    continue

                button.click()
                #driver.execute_script("arguments[0].click();", button)
                logging.warning("...building started!")
            except:
                logging.warning("Not enough resources")

            close_building(driver)

        lock.release()
        time.sleep(interval)