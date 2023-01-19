import time
import random

import src.constants as const

def wait(multiplicator:int=1):
    time.sleep(random.uniform(0.1, const.DELAY*multiplicator))