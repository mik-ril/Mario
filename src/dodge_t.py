import time
import logging

import undetected_chromedriver

from src.village import *
from src.troops import send_troops

def check_attack(driver:uc.Chrome):
    villagelist=driver.find_element(By.ID, 'villageList')
    prop=villagelist.get_attribute('ng-class')
    if prop=="{ongoingAttack: ongoingAttack}":
        logging.warning("Found incoming attack(s)")
        return True
    else:
        logging.warning("No incoming attacks")
        return False

def check_village(driver:uc.Chrome):
    driver.find_element(By.ID, "villageOverview").click()
    wait()

    villages=driver.find_elements(By.CSS_SELECTOR, 'tr[ng-repeat="village in overview | orderBy:\'villageName\'"]')
    under_attack=[]
    for i in range(len(villages)):
        try:
            attacks=villages[i].find_element(By.CSS_SELECTOR, 'i[ng-if="village.attacks.underAttack > 0"]')
            attack=str(attacks.get_attribute('tooltip-data')).encode('ascii','ignore')
            under_attack.append(i)
            logging.warning(f'found {attack} attacks on village {i}')
        except:
            pass

    driver.find_element(By.CSS_SELECTOR,'a[clickable="closeWindow(\'villagesOverview\')"]').click()
    wait()
    return under_attack

def check_time(driver:uc.Chrome, under_attack:list):
    pass