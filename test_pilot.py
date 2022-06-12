
"""
Import the subprocess module to execute the secure shell command with standard IOE 
"""

import subprocess

"""
# Getting input from user using input to pass the following functions

"""

print("Enter the Hostname/IP")

hostname = input("Enter HERE : ")

#print(hostname)

'Creating string for hostname/IP'
hostname_nmap = hostname + "_nmap.xml"
print(hostname_nmap)


"""
predefine nmap command as arguments in nmap_opt_1 variable
"""

"""
nmap_opt_one_command = "nmap"
nmap_opt_one_options = ["-sV","-sC","-T4"]
nmap_opt_basic = "nmap -sV -sC -T4 {0} -oX {1}".format(hostname,hostname_nmap)
"""
'The Following code should be used for invoke Nmap command with hostname variable with Shell=True, In future use DEVNULL for STDOUT AND STDERR'
nmap_opt_basic = "nmap -sV -sC -T4 {0} -oX {1}".format(hostname,hostname_nmap)

#nmap_opt_one_out = subprocess.run("nmap -sV -sC -T4 {0} -oX {1}".format(hostname,hostname_nmap),stdout=subprocess.PIPE,shell=True)

nmap_opt_one_out = subprocess.run(nmap_opt_basic,stdout=subprocess.PIPE,shell=True)

#print(nmap_opt_one_out)


#nmap_opt_one_out = subprocess.Popen([nmap_opt_one_command,nmap_opt_one_options,hostname],stdout= subprocess.PIPE)

#nmap_opt_one_out = subprocess.run([nmap_opt_one_command,nmap_opt_one_options,hostname],stdout= subprocess.PIPE)


