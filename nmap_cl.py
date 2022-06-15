
import subprocess


print("Enter the Hostname/IP")
hostname = input("Enter HERE : ")
print("Nmap Scan Type: Basic = b, Medium = m, Advance = a")
nmap_type = input("Enter Here the type: ")
#hostname_nmap = hostname + "_nmap.xml"

class nmap():
    def __init__(self,hostname,**args):
        self.hostname=hostname
        self.hostname_nmap_basic = hostname + "_nmap_basic.xml"
        self.hostname_nmap_medium = hostname + "_nmap_medium.xml"
        self.hostname_nmap_advance = hostname + "_nmap_advance.xml"
    def nmap_basic(self):
        self.nmap_opt_one_out = subprocess.run("nmap -sV -sC -T4 {0} -oX {1}".format(self.hostname,self.hostname_nmap_basic),stdout=subprocess.PIPE,shell=True)

    def nmap_medium(self):
        self.nmap_opt_one_out = subprocess.run("nmap -sV -sC -T4  --script vuln {0} -oX {1}".format(self.hostname,self.hostname_nmap_medium),stdout=subprocess.PIPE,shell=True)

    def nmap_advance(self):
        self.nmap_opt_one_out = subprocess.run("nmap -sV -sC -T3 -Pn --script vuln -p- {0} -oX {1}".format(self.hostname,self.hostname_nmap_advance),stdout=subprocess.PIPE,shell=True)



"""
Calling object within if else condition for switching object acording to user nmap parameter

"""

obj1=nmap(hostname)  #main Object of nmap class
if nmap_type == "b":
    obj1.nmap_basic()
elif nmap_type == "m":
    obj1.nmap_medium()
elif nmap_type == "a":  
    obj1.nmap_advance()
else :
    print("Options not provided")
