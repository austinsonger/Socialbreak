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

# Gmail
if [ -d gemailhack ]; then
        echo "Directory Gemail-Hack exists.[✔]"
# Facebook
if [ -d fbbrute ]; then
        echo "Directory Facebook Bruteforce exists.[✔]"
# Instainsane
fi [ -d instainsane ]; then
        echo "Directory instainsane exists.[✔]"
        cd instainsane
        chmod +x instainsane.sh
        cd ..
# TweetShell
fi [ -d tweetshell ]; then
        echo "Directory tweetshell  exists.[✔]"       
        cd tweetshell
        chmod +x tweetshell.sh
        cd ..

