from selenium.webdriver.common.keys import Keys
import time
import logging

from src.village import *
import src.constants as const

def send_troops(
        driver:uc.Chrome,
        village :int,
        target  :list,
        troops  :list,
        mode    :int
):

    logging.warning("Trying to send troops...")
    if ((target!=None) and (village!=None)):
        open_village(driver,village)
        open_village_city(driver)
        open_building(driver, const.RALLYPOINT)

        driver.find_element(By.CSS_SELECTOR,'button[clickable="openWindow(\'sendTroops\')"]').click()
        input=driver.find_element(By.XPATH, '/html/body/div[3]/window/div/div/div[4]/div/div/div[1]/div/div[1]/div[1]/span/input')

        #village not found error without this trick
        input.click()
        input.send_keys("")
        input.clear()
        wait()

        input.send_keys("({}|{})".format(target[0], target[1]))
        input.send_keys(Keys.ENTER)
        wait()

    for troop in troops:
        try:
            container=driver.find_element(By.CSS_SELECTOR, 'tbody[class="originalTroops"]')
            if troop[0]+1==11:
                container=container.find_element(By.CSS_SELECTOR, 'td[class="hero"]')
            else:
                container=container.find_element(By.CSS_SELECTOR, f'td[class="unit{troop[0]+1}"]')
            elements=container.find_elements(By.CSS_SELECTOR,'*')
            maxtroop=str(elements[1].get_attribute('innerHTML')).encode('ascii','ignore')

            #if -1 send everything
            if troop[1]==-1:
                driver.find_element(By.CSS_SELECTOR,f'input[class="unitInput{troop[0]}"]').send_keys(int(maxtroop))
            else:
                driver.find_element(By.CSS_SELECTOR,f'input[class="unitInput{troop[0]}"]').send_keys(troop[1])
                #if not enough troops do not send
                if int(maxtroop)<troop[1]:
                    logging.warning("Not enough troops: mission aborted")
                    close_rally(driver)
                    return

        except:
            logging.warning(f"Troop type {troop[0]} not available")

    #select mission type
    try:
        driver.find_element(By.CSS_SELECTOR,f'div[class="clickableContainer missionType{const.MODE[mode]}"]').click()
    except:
        logging.warning("Mission type not available, aborting!")
        close_rally(driver)
        return

    #try to send: if everything is right the button will be available
    try:
        driver.find_element(By.CSS_SELECTOR, 'button[class="next clickable"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'button[class="sendTroops clickable"]').click()
        logging.warning("... sent!")
    except:
        logging.warning("Something wrong: button disabled")
        close_rally(driver)