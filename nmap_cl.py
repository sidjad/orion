
import subprocess


print("Enter the Hostname/IP")
hostname = input("Enter HERE : ")
#hostname_nmap = hostname + "_nmap.xml"

class nmap():
    def __init__(self,hostname,**args):
        self.hostname=hostname
        self.hostname_nmap = hostname + "_nmap.xml"
    def nmap_basic(self):
        self.nmap_opt_one_out = subprocess.run("nmap -sV -sC -T4 {0} -oX {1}".format(self.hostname,self.hostname_nmap),stdout=subprocess.PIPE,shell=True)



   

obj1=nmap(hostname)
obj1.nmap_basic()
