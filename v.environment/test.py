from ast import Try
from distutils.command.clean import clean
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

        for i in range(4):
            #print(i)
            orangeWipe()
            time.sleep(1)
        if i == 3:
            i == 0 
            for i in range(4):
                #print(i)
                blueWipe()
                time.sleep(1)
            if i == 3:
                i == 0
                for i in range(4):
                    yellowWipe()
                    time.sleep(1)
                if i == 3:
                    i == 0
                    for i in range(4):
                        #print(i)
                        greenWipe()
                        time.sleep(1)
                    if i == 3:
                        i == 0
                        for i in range(4):
                            #print(i)
                            CyanWipe()
                            time.sleep(1)
                        if i == 3:
                            i == 0
                            for i in range(4):
                                #print(i)
                                PinkWipe()
                                time.sleep(1)    
except KeyboardInterrupt:
    clean




#while True:
    #TestWipe()
    
    

