#Das Programm soll ein Auswahlmenü haben, um ein Password zu generieren und dieses Unter einem Namen auf einer sql Lite Datenbank zu speichern.
#!/usr/bin/env python3
# coding: utf-8
from datetime import date
from optparse import Values
from ssl import _PasswordType
from tkinter import *
from sqlite3 import Error
import time
import secrets
import sqlite3
from tkinter.tix import InputOnly

verbindung = sqlite3.connect("PWdaten.db")
zeiger = verbindung.cursor()
today = date.today()
master = Tk()
master.geometry("400x180") #Anweisung größe des Bildes

# dd/mm/YY
act_day = today.strftime("%d/%m/%Y")
#print("actual day =", act_day)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
sql_anweisung = """
CREATE TABLE IF NOT EXISTS Passwörter (
Account VARCHAR(20), 
Passwort VARCHAR(30), 
Erstelldatum DATE
);"""
zeiger.execute(sql_anweisung)
#akutelle Werte der DB committen(Übertragen)
#verbindung.commit()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def sql_connection(): #Verbinden mit der Datenbank 
    try:
        con = sqlite3.connect(':memory:')
        time.sleep(3)
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    finally:
        con.close()
sql_connection()
#Zeige die aktuellen Einträge an!!!! Noch ab ändern  in SELECT statt der function 
def show_entry_fields():
   print("Account: %s\nPasswort: %s" % (Account, Passwort))
show_entry_fields()
#password generieren
def create_password(pw):
    crpassword = secrets.token_urlsafe(30)
    time.sleep(2)
    print("The Password is", crpassword)
#Eintrag hinzufügen
def add_entry():
    zeiger.execute()
    result = zeiger.fetchall
#checke ob der nutzer schon existiert
    if int(result[0]) > 0:
        error["text"] = "Error: Account wurde bereits angelegt"
    else:
        error["text"] = "Account mit Passwort angelegt" 
        zeiger.execute("INSERT INTO Passwörter(Account, Passwort)VALUES(?,?)", (Account, crpassword))
        verbindung.commit()  
#Error Erzeugen
error = Message(text="", width=160)
error.place(x = 30, y = 10)
error.config(padx=0)

Label(master, text="Account").grid(row=0)
Label(master, text="Passwort").grid(row=1)

Account = Entry(master)
Passwort = Entry(master)

Account.grid(row=0, column=1)
Passwort.grid(row=1, column=1)

Button(master, text='Speichern', command= add_entry).grid(row=3, column=0, sticky=W, pady=4) 
Button(master, text='Beenden', command=master.quit).grid(row=3, column=1, sticky=W, pady=4) 
Button(master, text='Anzeigen', command=show_entry_fields).grid(row=3, column=2, sticky=W, pady=4)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 