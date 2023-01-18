import os, subprocess

# p = subprocess.Popen('ping -n 1 127.0.0.1')
# p.wait()
# print(p.poll())

def _ping(netAddr):
    response = subprocess.check_output(['ping', '-n', '1', netAddr],stderr=subprocess.STDOUT, universal_newlines=True)
    return response

print(_ping("192.168.123.216"))