




#Nmap Class
import subprocess


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

obj1=nmap(hostname)  #main Object of nmap class
if nmap_type == "b":
    obj1.nmap_basic()
elif nmap_type == "m":
    obj1.nmap_medium()
elif nmap_type == "a":  
    obj1.nmap_advance()
else :
    print("Options not provided")

#Dnsenum Class
class dnsen():
    def __init__(self,hostname,**args):
        self.hostname=hostname
        self.hostname_dnsen = hostname + "_dnsenum.xml"
    def dnsen_basic(self):
        self.dnsen_opt_one_out = subprocess.run("dnsenum {0} -o {1}".format(self.hostname,self.hostname_dnsen),stdout=subprocess.PIPE,shell=True)

obj1=dnsen(hostname)
obj1.dnsen_basic()

"""
#Dnsdumpster

class dnsdumpster():
    def __init__(self,hostname,**args):
        self.hostname = hostname

"""
"""
#raccon tool ==>>  raccoon -d --vulners-nmap-scan --no-url-fuzzing --no-sub-enum -o /home/kali/test_out hostname
class racc():
    def __init__(self,hostname,**args):
        self.hostname=hostname
        self.hostname_reccon = hostname + "_raccon.txt"
    
    def raccon_reco(self):
        self.raccon_reco_out = subprocess.run("raccoon -d --vulners-nmap-scan --no-url-fuzzing --no-sub-enum -o /home/kali/test_out/{1} {0}.".format(self.hostname,self.hostname_reccon),stdout=subprocess.PIPE,shell=True)


obj1=racc(hostname)
obj1.raccon_reco()

"""
class subenum():
    def __init__(self,hostname,**args):
        self.hostname=hostname
        
    def subenum_reco(self):
        self.subenum_reco_out = subprocess.run(" subenum.sh -d {0} -r".format(self.hostname),stdout=subprocess.PIPE,shell=True)

obj1=subenum(hostname)
obj1.subenum_reco()




