import os, platform, subprocess, sys

from multiprocessing import Pool, current_process
import time

# p = subprocess.Popen('ping -n 1 127.0.0.1')
# p.wait()
# print(p.poll())

# print("Name of the operating system:", os.name)
# print("Name of the OS system:", platform.system())

N_HOSTS = 255

argv = sys.argv
if len(argv) != 2:
    print("Add the network address")
    exit()


def FilterList(string):
    list = string.replace("    ", "").splitlines()
    removeAll(list, "")
    return list


def removeAll(the_list, val):
    for i in range(the_list.count(val)):
        the_list.remove(val)


def _ping(hostAddr):
    response = None
    flag = "-n"
    if os.name == "posix":
        flag = "-c"
    try:
        response = subprocess.check_output(
            ["ping", flag, "1", hostAddr],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )

        response = FilterList(response)
        response = response[len(response) - 2].replace(" ", "").split(",")
        # print(response)

        toCheck = "ricevuti=1"
        if os.name == "posix":
            toCheck = "1packetsreceived"

        if response[1].lower() == toCheck:
            print("Host: " + hostAddr)

        response = 1
    except:
        response = -1
    return response


def ListAllHosts(netAddr):
    l = []
    for i in range(0, N_HOSTS):
        l.append(netAddr + str(i + 1))

    return l


def TruncateNet(addr):
    ipOct = addr.split(".")
    return f"{ipOct[0]}.{ipOct[1]}.{ipOct[2]}."


def work_log(work_data):
    ID = work_data.split(".")[3]

    # print("Process %s pinging %s" % (ID, work_data))
    status = _ping(work_data)
    # print("Process %s Finished." % ID)


def pool_handler():
    p = Pool(50)
    p.map(work_log, list_hosts)


list_hosts = []


if __name__ == "__main__":
    list_hosts = ListAllHosts(TruncateNet(argv[1]))
    # print(list_hosts)
    pool_handler()

    print("LAN checked")
    """
    response = subprocess.check_output(
        ["nslookup", "192.168.0.1"],
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    print(response)
    """
