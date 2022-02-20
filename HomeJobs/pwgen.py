#Das Programm soll ein Auswahlmenü haben, um ein Password zu generieren und dieses Unter einem Namen auf einer sql Lite Datenbank zu speichern.

import secrets
import sqllite


def create_password(pw):
    password = secrets.token_urlsafe(32)
    print("The Password is", password)
