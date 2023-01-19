import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from src.utility import wait
import src.constants as const

def login(driver:uc.Chrome):
    driver.get(const.BASE_URL)

    driver.find_element(By.XPATH, "//*[@id='cmpbntyestxt']").click()
    driver.find_element(By.XPATH, "//*[@id='loginButton']").click()
    wait()

    frame = driver.find_element(By.XPATH, "//*[starts-with(@id,'easyXDM_default')]")
    driver.switch_to.frame(frame)
    frame = driver.find_element(By.XPATH, "/html/body/iframe")
    driver.switch_to.frame(frame)
    driver.find_element(By.NAME, 'email').send_keys(const.USER_MAIL)
    driver.find_element(By.NAME, 'password').send_keys(const.USER_PWD)
    driver.find_element(By.NAME, 'submit').click()
    driver.switch_to.parent_frame()
    driver.switch_to.parent_frame()
    wait()

    #remove save credential notification
    #driver.find...
    #driver.click...
    driver.find_element(By.CSS_SELECTOR, 'div.row:nth-child(3) > div:nth-child(1) > div:nth-child(1)').click()
    wait()

    try:
        driver.find_element(By.CSS_SELECTOR, 'a[clickable="closeWindow(\'welcomeScreen\')"]').click()
        wait()
    except:
        pass

def tribe(driver:uc.Chrome):
    driver.find_element(By.ID, 'userNameButton').click()

    info=driver.find_element(By.XPATH, '/html/body/div[3]/window/div/div/div[4]/div/div/div[1]/div/div/div/div/div/div/player-profile/div/div/div/div[3]/div[1]/div/div[2]/div[5]/span[2]')
    mytribe=int(info.get_attribute('options').encode('ascii','ignore'))
    driver.find_element(By.CSS_SELECTOR, 'a[clickable="closeWindow(\'profile\')"]').click()
    return mytribe