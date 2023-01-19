from selenium.webdriver.common.keys import Keys
import time
import logging

from src.village import *
import src.constants as const

def select_and_train(
        driver   : uc.Chrome,
        reference: int,
        troop    : list
):
    driver.find_element(By.CSS_SELECTOR, f'img[data="{reference + troop[0]}"]').click()
    wait()
    fill = driver.find_element(By.CSS_SELECTOR, 'input.value')
    fill.clear()
    if troop[1]==-1:
        driver.find_element(By.CSS_SELECTOR, 'div[class="iconButton maxButton clickable"]').click()
    else:
        fill.send_keys(troop[1])
    try:
        driver.find_element(By.CSS_SELECTOR, 'button[clickable="startTraining(activeItem)"]').click()
    except:
        logging.warning(f'The button was not active for troop {troop[0]}')


def train_troops(
        driver    :uc.Chrome,
        tribe     :int,
        village   :int,
        troops    :list
):

    open_village(driver, village)
    open_village_city(driver)

    #this number is increasing: legio=1 -> club=11 -> phalanx=21
    reference=10*(tribe-1)+1
    if tribe==1:
        for troop in troops:
            if troop[0]==0 or troop[0]==1 or troop[0]==2:
                open_building(driver, const.BARRAKS)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==3 or troop[0]==4 or troop[0]==5:
                open_building(driver, const.STABLE)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==6 or troop[0]==7:
                open_building(driver, const.WORKSHOP)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==8 or troop[0]==9:
                open_building(driver, const.RESIDENCE)
                select_and_train(driver, reference, troop)
                close_building(driver)
            else:
                logging.warning(f"Troop {troop[0]} invalid!")
        logging.warning("... training started!")

    elif tribe==2:
        for troop in troops:
            if troop[0]==0 or troop[0]==1 or troop[0]==2 or troop[0]==3:
                open_building(driver, const.BARRAKS)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==4 or troop[0]==5:
                open_building(driver, const.STABLE)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0] == 6 or troop[0] == 7:
                open_building(driver, const.WORKSHOP)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==8 or troop[0]==9:
                open_building(driver, const.RESIDENCE)
                select_and_train(driver, reference, troop)
                close_building(driver)
            else:
                logging.warning(f"Troop {troop[0]} invalid!")
        logging.warning("... training started!")

    elif tribe==3:
        for troop in troops:
            if troop[0]==0 or troop[0]==1:
                open_building(driver, const.BARRAKS)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==2 or troop[0]==3 or troop[0]==4 or troop[0]==5:
                open_building(driver, const.STABLE)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==6 or troop[0]==7:
                open_building(driver, const.WORKSHOP)
                select_and_train(driver, reference, troop)
                close_building(driver)
            elif troop[0]==8 or troop[0]==9:
                open_building(driver, const.RESIDENCE)
                select_and_train(driver, reference, troop)
                close_building(driver)
            else:
                logging.warning(f"Troop {troop[0]} invalid!")
        logging.warning("... training started!")

    else:
        logging.warning("Tribe not found!")