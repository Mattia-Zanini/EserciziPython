import os, subprocess

# p = subprocess.Popen('ping -n 1 127.0.0.1')
# p.wait()
# print(p.poll())

def FilterList(string):
    list = string.replace("    ", "").splitlines()
    removeAll(list, "")
    return list

def removeAll(the_list, val):
    for i in range(the_list.count(val)):
        the_list.remove(val)

def _ping(hostAddr):
    response = None
    try:
        response = subprocess.check_output(['ping', '-n', '1', hostAddr], stderr=subprocess.STDOUT, universal_newlines=True)
        
        response = FilterList(response)
        response = response[len(response) - 2].replace(" ", "").split(",")
        if response[1].lower() == "ricevuti=1":
            print("Host: " + hostAddr)
        
        response = 1
    except:
        response = -1
    return response

def PingAllHosts(netAddr):
    hosts = []
    for i in range(1, 5):
        status = _ping(netAddr + str(i))

PingAllHosts("192.168.235.")