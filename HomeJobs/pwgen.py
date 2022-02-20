#Das Programm soll ein Auswahlmenü haben, um ein Password zu generieren und dieses Unter einem Namen auf einer sql Lite Datenbank zu speichern.
#!/usr/bin/env python3
# coding: utf-8
from datetime import date
from optparse import Values
from tkinter import *
import secrets
import sqlite3

verbindung = sqlite3.connect("PWdaten.db")
zeiger = verbindung.cursor()
today = date.today()

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
verbindung.commit()
#verbindung zur DB schließen
verbindung.close()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

def show_entry_fields():
   print("Account: %s\nPasswort: %s" % (Account.get(), Passwort.get()))

def add_entry():
    password = secrets.token_urlsafe(32)
    print("The Password is", password)
    Account = Account.get()
    Passwort = Passwort.get()
    zeiger.execute("SELECT COUNT(*) from Passwörter WHERE Account = ' "+ Account +"' ")
    zeiger.execute("SELECT COUNT(*) from Passwörter WHERE Passwort = ' "+ password +"' ")
    result = zeiger.fetchall

#checking ob der nutzer schon existiert
    if int(result[0]) > 0:
        error["text"] = "Error: Account wurde bereits angelegt"
    else:
        error["text"] = "Account mit Passwort angelegt" 
        zeiger.execute("INSERT INTO Passwörter(Account, Passwort)VALUES(?,?)", (Account, password))
        verbindung.commit()  

master = Tk()
master.geometry("400x180")

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

Button(master, text='Speichern', command= add_entry).grid(row=3, column=0, sticky=W, pady=4) #quit durch Speichern ersetzen
Button(master, text='Beenden', command=master.quit).grid(row=3, column=1, sticky=W, pady=4) 
Button(master, text='Anzeigen', command=show_entry_fields).grid(row=3, column=2, sticky=W, pady=4)

mainloop( )
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#password generieren
#def create_password(pw):
#    password = secrets.token_urlsafe(32)
#    print("The Password is", password)