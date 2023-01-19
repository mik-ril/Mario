import threading
from threading import Thread

import undetected_chromedriver as uc

from src.robbers_t import thread_robbers
from src.adventures_t import thread_adventures
from src.supply_t import thread_supply
from src.train_t import thread_train
from src.farming_t import thread_farming
from src.building_t import thread_building

from src.login import login, tribe

class Mario():

    #constructor and login
    def __init__(self):
        super(Mario, self).__init__()
        self.driver=uc.Chrome()

        self.lock=threading.Lock()

        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()

        login(self.driver)
        self.tribe=tribe(self.driver)

    def __enter__(self):
        return self

    #destructor
    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.driver.quit()
        pass

    #robber camps
    def robber_slayer(self, village:int, troops:list, mode:int=1, interval:int=1000):
        Thread(
            target=thread_robbers,
            name="robber slayer",
            args=[self.lock, self.driver, village, troops, mode, interval]
        ).start()

    #adventures
    def adventure_time(self, health:int=30, interval:int=1000):
        Thread(
            target=thread_adventures,
            name="adventure time",
            args=[self.lock, self.driver, health, interval]
        ).start()

    #supply
    def sharing_is_caring(self, source:int, target:list, quantity:list, interval:int=1000):
        Thread(
            target=thread_supply,
            name="sharing is caring",
            args=[self.lock, self.driver, source, target, quantity, interval]
        ).start()

    #train troops
    def the_bigger_they_are(self, village:int, troops:list, interval:int=1000):
        Thread(
            target=thread_train,
            name="the bigger they are",
            args=[self.lock, self.driver, self.tribe, village, troops, interval]
        ).start()

    #farmlist
    def the_harder_they_fall(self, village:int, troops:list, interval:int=1000):
        Thread(
            target=thread_farming,
            name="the harder they fall",
            args=[self.lock, self.driver, village, troops, interval]
        ).start()

    #build stuff
    def bob_the_builder(self, buildings:list, interval:int=1000):
        Thread(
            target=thread_building,
            name="bob the builder",
            args=[self.lock, self.driver, buildings, interval]
        ).start()