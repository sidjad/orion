with open ("active_ip.py") as file:
    for x in file:
        sub_host = x
        print(sub_host.rstrip())
