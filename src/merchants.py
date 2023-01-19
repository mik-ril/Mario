from selenium.webdriver.common.keys import Keys
import logging

from src.village import *
import src.constants as const

def send_resources(
        driver:   uc.Chrome,
        source:   int,
        target:   list,
        quantity: list
):
    open_village(driver, source)
    open_village_city(driver)
    open_building(driver, const.MARKET)

    if target[0]!=None:
        input=driver.find_element(By.XPATH, '/html/body/div[3]/window/div/div/div[4]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/table[2]/tbody/tr[2]/td[1]/span/input')

        input.click()
        input.send_keys("")
        input.clear()
        wait()

        input.send_keys("({}|{})".format(target[0], target[1]))
        input.send_keys(Keys.ENTER)
        wait()

    # target is own [None, village]
    elif target[0]==None:
        driver.find_element(By.CSS_SELECTOR, 'a[ng-if="showOwnVillages"]').click()
        #implement here

    else:
        logging.warning("Format unknown!")

    bars=driver.find_elements(By.CSS_SELECTOR, 'tr[ng-repeat="(resourceType, resName) in resNames"]')
    iterator=0
    for bar in bars:
        input=bar.find_element(By.CSS_SELECTOR, 'input[type="tel"]')
        input.clear()
        input.send_keys(quantity[iterator])
        iterator+=1

    try:
        #CHECK IS the CSS is RIGHR
        driver.find_element(By.CSS_SELECTOR, 'button[class="clickable"]').click()
        logging.warning("... resources sent!")
    except:
        logging.warning("Could not send resources, button disabled!")