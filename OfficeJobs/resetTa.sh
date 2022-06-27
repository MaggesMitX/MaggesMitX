#!/bin/bash

echo  "--------------------------------------------------------"
echo  "------------------------ATTENTION-----------------------" 
echo  "----- THIS SCRIPT DELETE ALL DOCKER VOLUMES OF TA ------"
echo  "------------- AND PULLS THE NEWEST IMAGES  -------------"
echo  "--------------------------------------------------------"

if [ ${EUID:-$(id -u)} -eq 0 ]
then
  echo "SURE ? - Press Enter"
  read enterKey
  echo "Shutting down container..."
  docker-compose -f /opt/ta/docker-compose.yml down
  echo "Removing volumes..."
  docker volume prune -f
  echo "Pulling new container... [this may take a few minutes]"
  docker-compose -f /opt/ta/docker-compose.yml pull
  echo "-----------------------------------------------------------------------------------------"
  echo "All volumes are reset and the (new) container are pulled. Please deploy new customer now!"
  echo "-----------------------------------------------------------------------------------------"
else
  echo "If you are brave - Please run as root"
  exit
fi

