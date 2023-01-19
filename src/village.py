import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from src.utility import wait
import src.constants as const

def open_village(driver:uc.Chrome, index:int):
    driver.find_element(By.ID,'villageOverview').click()
    wait()

    table=driver.find_element(By.CSS_SELECTOR, 'table[class="villagesTable lined"]')
    villages=table.find_elements(By.CSS_SELECTOR, 'a[class="truncated clickable"]')
    villages[index].click()
    wait()

    driver.find_element(By.CSS_SELECTOR,'a[clickable="closeWindow(\'villagesOverview\')"]').click()
    wait()

def open_village_city(driver:uc.Chrome):
    check=driver.find_element(By.ID, 'optimizly_mainnav_village')
    if check.get_attribute('class')!='navi_village bubbleButton active':
        driver.find_element(By.XPATH, "//*[@id=\"optimizly_mainnav_village\"]").click()
        wait()
    else:
        pass

def open_village_resources(driver:uc.Chrome):
    check=driver.find_element(By.ID, 'optimizly_mainnav_resources')
    if check.get_attribute('class')!='navi_resources bubbleButton active':
        driver.find_element(By.XPATH, "//*[@id=\"optimizly_mainnav_resources\"]").click()
        wait()
    else:
        pass

def open_building(driver:uc.Chrome, index:int):
    #special method: click alone returns "click intercepted"
    #but for some arcane reasons the execute_script works
    area=driver.find_element(By.CSS_SELECTOR, f'area[building-positioner="{index}"]')
    driver.execute_script("arguments[0].click();", area)
    wait()

def close_building(driver:uc.Chrome):
    driver.find_element(By.CSS_SELECTOR, 'a[clickable="closeWindow(\'building\')"]').click()
    wait()

def close_rally(driver:uc.Chrome):
    driver.find_element(By.CSS_SELECTOR,'a[clickable="closeWindow(\'sendTroops\')"] ').click()
    wait()

def open_map(driver:uc.Chrome):
    driver.find_element(By.XPATH, '//*[@id="optimizly_mainnav_map"]').click()
    wait()