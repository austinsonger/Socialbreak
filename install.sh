#!/bin/bash
#Sysupdate
sudo apt-get update 
#APT
sudo apt install -y \
    python \
    python3-pip \ 
    tor \
    curl \
    openssl \

# PIP
sudo pip install bs4
sudo pip install mechanize
sudo pip install requests

