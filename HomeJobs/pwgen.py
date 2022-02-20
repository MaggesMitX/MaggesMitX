#Das Programm soll ein Auswahlmenü haben, um ein Password zu generieren und dieses Unter einem Namen auf einer sql Lite Datenbank zu speichern.

import secrets
import sqlite3

verbindung = sqlite3.connect("PWdaten.db")
zeiger = verbindung.cursor()

sql_anweisung = """
CREATE TABLEIF NOT EXISTS Passwörter (
Account VARCHAR(20), 
Passwort VARCHAR(30), 
Erstelldatum DATE
);"""

zeiger.execute(sql_anweisung)
#akutelle Werte der DB committen(Übertragen)
verbindung.commit()
#verbindung zur DB schließen
verbindung.close()


#password generieren
def create_password(pw):
    password = secrets.token_urlsafe(32)
    print("The Password is", password)
