#!/bin/bash

echo  "--------------------------------------------------------"
echo  "------------------------ATTENTION-----------------------" 
echo  "--------- Update Ubuntu Server automaticaly ------------"
echo  "--------------------------------------------------------"

if [ ${EUID:-$(id -u)} -eq 0 ]
then
    if nc -zw1 google.com 443;
    then
      echo "we have connectivity"
      echo "Update wird geladen, prüfe ob eine Internetverbindung besteht"
      echo "-----------------------------------------------------------------------------------------"
      echo "Update wird gestartet!"
      echo "-----------------------------------------------------------------------------------------"
      echo sudo apt Update && sudo apt full-upgrade
      echo sudo apt autoremove
      echo sudo apt autoclean
      echo "-----------------------------------------------------------------------------------------"
      echo "Update Abgeschlossen, System wird neugestartet."
      echo "-----------------------------------------------------------------------------------------"
      echo sudo reboot
      fi
    else
      echo "Fehler!, Es konnte keine Verbindung mit dem Internet hergestellt werden.Bitte Prüfe deine Internetverbindung"
      exit
else
echo "If you are brave - Please run as root"