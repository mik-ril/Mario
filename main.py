from src.mario import Mario

import time

from src.dodge_t import check_attack, check_village

with Mario() as bot:
    #bot.robber_slayer(0,[[0,-1],[1,-1],[10,1]],1,3600)
    #bot.adventure_time(interval=1200)
    #bot.the_bigger_they_are(0,[[0,-1],[9,2]])
    #bot.the_harder_they_fall(0, [[0,5],[1,4]])
    bot.bob_the_builder([[1, 1, 5],
                         [1, 2, 5],
                         [1, 4, 5],
                         [1, 5, 5],
                         ],interval=300)

    #check_village(bot.driver)

    #needs implementation
    #bot.sharing_is_caring(0,[-26,25],[10,30,50,70])

    #to do for evading troops
    #keep_Summer_safe

    time.sleep(10)
