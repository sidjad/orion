
import subprocess


print("Enter the Hostname/IP")
hostname = input("Enter HERE : ")


class dnsen():
    def __init__(self,hostname,**args):
        self.hostname=hostname
        self.hostname_dnsen = hostname + "_dnsenum.xml"
    def dnsen_basic(self):
        self.dnsen_opt_one_out = subprocess.run("dnsenum {0} -o {1}".format(self.hostname,self.hostname_nmap),stdout=subprocess.PIPE,shell=True)



   

obj1=dnsen(hostname)
obj1.dnsen_basic()
