import os
def install():
	os.system("apt update")
	os.system("apt install python3-pip")
	os.system("apt install tor -y")
	os.system("apt install curl -y")
	os.system("apt install openssl -y")
	os.system("pip install mechanize")
	os.system("pip install requests")
    os.system("pip istall cookielib")
	os.system("pip install bs4") 
    os.system("pip install banner")
	os.system("apt install perl -y")
	print "\n"
	print """Preparing"""
	i = raw_input("press ctrl c to stop hit enter to continue")
install()
