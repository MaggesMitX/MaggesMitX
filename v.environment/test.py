from ast import Try
from distutils.command.clean import clean
from itertools import cycle
from pickle import GLOBAL
import time 
i = 0

#<------------------------------------------------------->
def Testlauf():
    print("Untergeordnete Funktion läuft")

#<------------------------------------------------------->

def PinkWipe():
    print("PinkWipe", i ,"läuft")
    time.sleep(1)
    Testlauf()
    print("PinkWipe", i ,"läuft")

def CyanWipe():
    print("CyanWipe", i ,"läuft")
    time.sleep(1)
    Testlauf()
    print("CyanWipe", i ,"läuft")

def blueWipe():
    print("blueWipe", i ,"läuft")
    time.sleep(1)
    Testlauf()
    print("blueWipe", i ,"läuft")

def orangeWipe():
    print("orangeWipe", i ,"läuft")
    time.sleep(1)
    Testlauf()
    print("orangeWipe", i ,"läuft")

def yellowWipe():
    print("yellowWipe", i ,"läuft")
    time.sleep(1)
    Testlauf()
    print("yellowWipe", i ,"läuft")

def greenWipe():
    print("greenWipe", i ,"läuft")
    time.sleep(1)
    Testlauf()
    print("greenWipe", i ,"läuft")    
#<---------------------------------------------------------->

try:
    while True:
        orangeWipe()
        time.sleep(900)
        yellowWipe()
        time.sleep(900)
        greenWipe()
        time.sleep(900)
        CyanWipe()
        time.sleep(900)
        blueWipe()
        time.sleep(900)
        PinkWipe()
        time.sleep(900)
except KeyboardInterrupt:
    clean







# try:

#     while True:

#         for i in range(4):
#             #print(i)
#             orangeWipe()                            #Orange Wipe for Loop
#             time.sleep(1)
#         if i == 3:
#             i == 0 
#             for i in range(4):
#                 #print(i)
#                 blueWipe()                          #Blue Wipe for Loop
#                 time.sleep(1)
#             if i == 3:
#                 i == 0
#                 for i in range(4):
#                     yellowWipe()                    #Yellow Wipe for Loop
#                     time.sleep(1)
#                 if i == 3:
#                     i == 0
#                     for i in range(4):
#                         #print(i)
#                         greenWipe()                 #Green Wipe for Loop
#                         time.sleep(1)
#                     if i == 3:
#                         i == 0
#                         for i in range(4):
#                             #print(i)
#                             CyanWipe()              #Cyan Wipe for Loop
#                             time.sleep(1)
#                         if i == 3:
#                             i == 0
#                             for i in range(4):
#                                 #print(i)
#                                 PinkWipe()          #Pink Wipe for Loop
#                                 time.sleep(1)    
# except KeyboardInterrupt:
#     clean




#while True:
    #TestWipe()
    
    
