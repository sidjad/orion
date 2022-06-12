*This is a Logic which need multiple times in future 

import subprocess


print("Enter the Hostname/IP")
hostname = input("Enter HERE : ")


hostname_nmap = hostname + "_nmap.xml"
nmap_opt_one_out = subprocess.run("nmap -sV -sC -T4 {0} -oX {1}".format(hostname,hostname_nmap),stdout=subprocess.PIPE,shell=True)

