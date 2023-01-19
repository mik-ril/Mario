# Mario_the_bot

__Disclaimer:__ Please note that this is a research project. I am by no means responsible for any usage
of this tool, use it on your own behalf. I'm also not responsible if your accounts get banned due to extensive
use of this tool.

# Table of Contents
- [Introduction](#Introduction)
- [Getting Started](#Getting-Started)
- [Features](#Features)
- [Parameters and Conventions](#Parameters-and-Conventions)
    - [The DELAY Parameter](#The-DELAY-Parameter)
    - [Village Number](#Village-Number)
    - [Building Convention](#Building-Convention)
    - [Troop Convention](#Troop-Convention)
    - [Type of Attack](#Type-of-Attack)
- [Features](#Features)
    - [Attacking Robbers](#Attacking-Robbers)
    - [Adventures](#Adventures)
    - [Supply Resources](#Supply-Resources)
    - [Farm List](#Farm-List)
    - [Upgrading Buildings](#Upgrading-Buildings)
    - [Evading Troops](#Evading-Troops)

# Introduction
I consider myself no software developer, indeed I am not. Therefore do not expect the code to be written as
a real developer would have written it. I have some years of experience with C++ as complementary knowledge 
and I was interested in learning some python as well. However I was quite tired of pointless courses making
you write pointless programs, so I decided to learn (a really small portion) of python through field
applications. While making this decision I was playing Travian Kingdoms so here I am.

# Getting Started
I normally work on a Linux machine, and I don't have the time to test it on Windows, but I am sure Google has
all the answers you are looking for. Here some steps to get the bot working:

1. Install python3
    1.  [Get python](https://www.python.org/downloads/)
    2.  I am using 10.6 but unless you get an ancient release I guess anything will work
2. Install selenium
    1.  On a terminal run `python -m pip install selenium`
    2.  This package contains all the stuff for surfing the web
3. Install undetected-chromedriver
    1.  Download [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
    2.  This is what will (probably) not get you banned
    3.  Go thank the guys that have developed that code
4. Put your username and password
    1.  Open `src/constants.py`
    2.  Fill `USER_NAME` and `USER_PWD` variables with your data
    3.  I know it's annoying, I promise you I'm not stealing your credentials, go check the rest of the code
5.  Edit main
    1. Fpen `main.py`
    2. Fill with the activities you want the bot to perform while you're sleeping or enjoying a sunny day
  outside home
6. Run the script
    1. Just `python3 main.py` on a console is enough 
    
# Parameters and Conventions
## The DELAY Parameter
In the `src/constants.py` file you can find the `DELAY` parameter. Essentially, after every click the bot
will wait a random amount of time between zero seconds and `DELAY` seconds, for obvious purposes. You can
freely modify that number, keeping in mind that the Travian Police can spot if you're clicking
at ludicrous speed.

## Village Number
Most of the times you will need to tell the bot in which village you want to perform a certain action. To 
do so you will need to use an integer, starting from 0 (zero) and increasing in alphabetical order. However
I've noticed that most of the player already use numbers in naming village, starting from `00 "name"` so
it was quite natural to implement it in this way.

## Building Convention
In the `src/constants.py` file you can see that each building has an associated number. The problem here is
that in the HTML each slot has an associated number, independent on what you build on it. Hence, I've included
in the `media` folder a screenshot of the number associated *with each slot*. You can modify that numbers in
case your village (or camps) are different. No need to say that if you want to train troops in multiple
villages all your barraks have to be in the same slot.

## Troop Convention
The bot will automatically detect your tribe. If you need to send troops somewhere you will need to give 
a list of lists (which I'd simply call multi-dimensional array) as the following:
```
[[type,quantity],[type,quantity],[type,quantity],...]
```
How does it work? It's a mess, but I've tried my best. The `type` is the troop type, you can see from the
`src/constants.py` that it is an integer from 0 (legio/club/phala) from 10 (hero), and it is based on the
order you see when you are sending the troops from the rally. You do not need to specify "previous" troops:
if you want to send only 50 imperians (or axes or pathfinders) you  can go with `[[2,50]]`. Another important
point, if you want to send all the troops just put a -1 in the quantity.

If you need to train troops the variable is the same. As I said, the bot knows your tribe so it will know
which building to open (provided that the slot number is correct).

## Type of Attack
Again from `src/constants.py` file you can see the `MODE` variable. This express the attack tipe, and you
shall use it in the bot methods. In case you're not familiar with arrays, note that the first index is zero
so if you want to send a raid you have to use `MODE[2]` while a siege is `MODE[4]`.

    
# Features
Now, the juicy part. I will go in the description of all the methods of the bot, what they do and how to use
them. If you want to use a method just go in the `main.py` and add it, along with the others.

*The interval is expressed in seconds.*

A (more or less) technical detail: each method will start a thread, acquiring and releasing a lock to avoid 
simultaneous interaction with the webpage. after releasing the lock the thread will go to sleep for the
required time, before restarting. This is the best I could do with my small python experience (as I said
I'm really learning it right now, and I foud it terribly inconsistent compared to C++ but anyway). 

## Attacking Robbers
```python
#definition
def robber_slayer(self, village:int, troops:list, mode:int=1, interval:int=1000):

#in the main
bot.robber_slayer(0,[[0,-1],[1,50]],1,3600)
```
This method will search for robbers and automatically attack (mode=1) them. You just have to place the
village, i.e. your capital, and the troop list. In case you want to raid them just put a `mode=2`, and you
modify the interval for the execution of the code as you please.

## Adventures
```python
#definition
def adventure_time(self, health:int=30, interval:int=1000):

#in the main
bot.adventure_time()

#or for example
bot.adventure_time(health=20, interval=3600)
```
This will check if there are adventures available and if the hero has more health that the number you
placed (i.e. 30%). If all the lights are green, the hero is sent.

## Supply Resources
```python
#definition
def sharing_is_caring(self, source:int, target:list, quantity:list, interval:int=1000):

#in the main
bot.sharing_is_caring(0,[-26,25],[750,750,750,750], 7200)

#or for example
bot.sharing_is_caring(0,[None,1],[1500,1500,1500,750])
```
With this method you can send resources from a source village to a target one, every `interval` seconds.
In this case the village can be expressed with a couple of coordinates (the village is not yours) or 
using `[None, index]`, where `index` is the index of your village (not the source one of course). Then the 
resources to be sent are expressed as a list.

## Training Troops
```python
#definition
def the_bigger_they_are(self, village:int, troops:list, interval:int=1000):

#in the main
bot.the_bigger_they_are(0,[[0,10],[3,-1]])

#or for example
bot.the_bigger_they_are(0,[[0,10],[1,10],[2,10]], interval=360)
```
This methods train the list of troop you wrote in the village with the index you placed, every interval.
Easy peasy.

## Farm List 
```python
#definition
def the_harder_they_fall(self, village:int, troops:list, interval:int=1000):

#in the main
bot.the_harder_they_fall(0, [[0,5],[1,4]])

#or for example
bot.the_harder_they_fall(0, [[0,5],[1,4]], interval=3600)
```
This is for sending troops like in a farmlist, but without paying for premium or how the hell it is called. 
Place your farm coordinates in the `farmilist.txt`, placing a space between x and y. Select the village
you want to send from, the troops you want to send and that's it.

## Upgrading Buildings
```python
#definition
def bob_the_builder(self, buildings:list, interval:int=1000):

#in the main
bot.bob_the_builder([[0,9,5],[1,23,3]])
```
This is for upgrading buildings. Just that. The argument is a list of lists, each sublist contains: the village, the slot and the maximum level.
The bot will check if it possible to upgrade the selected slot, and if the current level is lower than the wanted one. Therefore, if you want to
upgrade a building to level 20 DO NOT write each level, just put a 20!
All the buildings are checked in sequence, and it is repeated after the chosen interval. Hence, if at some time the resources are not enough,
the upgrade may start later.

## Evading Troops
*Under development*

